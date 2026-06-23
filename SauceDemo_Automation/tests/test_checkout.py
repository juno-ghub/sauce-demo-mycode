import pytest
import logging
from config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

logger = logging.getLogger(__name__)


@pytest.fixture
def logged_in_driver_with_cart_items(driver):
    """Fixture to provide logged-in driver with items in cart"""
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart(0)
    products_page.go_to_cart()
    
    return driver


@pytest.mark.checkout
@pytest.mark.positive
@pytest.mark.smoke
class TestCheckoutPositive:
    """Positive test cases for checkout functionality"""
    
    def test_complete_checkout_flow(self, logged_in_driver_with_cart_items):
        """Test complete checkout flow"""
        logger.info("Starting test: Complete checkout flow")
        
        driver = logged_in_driver_with_cart_items
        cart_page = CartPage(driver)
        
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        
        checkout_page.fill_checkout_information("John", "Doe", "12345")
        checkout_page.click_continue()
        
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        checkout_page.click_finish()
        
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        assert checkout_page.is_order_confirmation_displayed(), "Order confirmation not displayed"
        
        logger.info("Test passed: Checkout flow completed successfully")
    
    def test_checkout_with_valid_information(self, logged_in_driver_with_cart_items):
        """Test checkout with valid information"""
        logger.info("Starting test: Checkout with valid information")
        
        driver = logged_in_driver_with_cart_items
        cart_page = CartPage(driver)
        
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        
        checkout_page.enter_first_name("Jane")
        checkout_page.enter_last_name("Smith")
        checkout_page.enter_postal_code("54321")
        
        checkout_page.click_continue()
        
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        assert "checkout-step-two" in driver.current_url, "Should proceed to checkout step two"
        
        logger.info("Test passed: Valid checkout information accepted")


@pytest.mark.checkout
@pytest.mark.negative
class TestCheckoutNegative:
    """Negative test cases for checkout functionality"""
    
    def test_checkout_with_empty_first_name(self, logged_in_driver_with_cart_items):
        """Test checkout with empty first name"""
        logger.info("Starting test: Checkout with empty first name")
        
        driver = logged_in_driver_with_cart_items
        cart_page = CartPage(driver)
        
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = checkout_page.get_error_message()
        assert "First Name is required" in error_msg, "First name required error not shown"
        
        logger.info("Test passed: Error displayed for empty first name")
    
    def test_checkout_with_empty_last_name(self, logged_in_driver_with_cart_items):
        """Test checkout with empty last name"""
        logger.info("Starting test: Checkout with empty last name")
        
        driver = logged_in_driver_with_cart_items
        cart_page = CartPage(driver)
        
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        
        checkout_page.enter_first_name("John")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = checkout_page.get_error_message()
        assert "Last Name is required" in error_msg, "Last name required error not shown"
        
        logger.info("Test passed: Error displayed for empty last name")
    
    def test_checkout_with_empty_postal_code(self, logged_in_driver_with_cart_items):
        """Test checkout with empty postal code"""
        logger.info("Starting test: Checkout with empty postal code")
        
        driver = logged_in_driver_with_cart_items
        cart_page = CartPage(driver)
        
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(driver)
        
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = checkout_page.get_error_message()
        assert "Postal Code is required" in error_msg, "Postal code required error not shown"
        
        logger.info("Test passed: Error displayed for empty postal code")

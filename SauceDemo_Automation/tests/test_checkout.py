import pytest
import logging
from config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

logger = logging.getLogger(__name__)


@pytest.mark.checkout
@pytest.mark.positive
class TestCheckoutPositive:
    """Positive test cases for checkout flow"""

    def test_complete_checkout_flow(self, driver):
        """Test complete checkout flow"""
        logger.info("Starting test: Complete checkout flow")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        checkout_page.click_finish()

        logger.info("Test passed: Checkout flow completed")


@pytest.mark.checkout
@pytest.mark.negative
class TestCheckoutNegative:
    """Negative test cases for checkout flow"""

    def test_missing_first_name(self, driver):
        """Test checkout without first name"""
        logger.info("Starting test: Missing first name")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()

        assert checkout_page.is_error_message_displayed(), "Error message should be shown"
        assert "first name" in checkout_page.get_error_message().lower(), "First name error not shown"

        logger.info("Test passed: Missing first name error displayed")

    def test_missing_last_name(self, driver):
        """Test checkout without last name"""
        logger.info("Starting test: Missing last name")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()

        assert checkout_page.is_error_message_displayed(), "Error message should be shown"
        assert "last name" in checkout_page.get_error_message().lower(), "Last name error not shown"

        logger.info("Test passed: Missing last name error displayed")

    def test_missing_postal_code(self, driver):
        """Test checkout without postal code"""
        logger.info("Starting test: Missing postal code")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.click_continue()

        assert checkout_page.is_error_message_displayed(), "Error message should be shown"
        assert "postal code" in checkout_page.get_error_message().lower(), "Postal code error not shown"

        logger.info("Test passed: Missing postal code error displayed")

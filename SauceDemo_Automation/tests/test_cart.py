import pytest
import logging
from config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

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
    products_page.add_product_to_cart(1)
    
    return driver


@pytest.mark.cart
@pytest.mark.positive
@pytest.mark.smoke
class TestCartPagePositive:
    """Positive test cases for cart functionality"""
    
    def test_view_cart_with_items(self, logged_in_driver_with_cart_items):
        """Test viewing cart with items"""
        logger.info("Starting test: View cart with items")
        
        driver = logged_in_driver_with_cart_items
        products_page = ProductsPage(driver)
        
        products_page.go_to_cart()
        cart_page = CartPage(driver)
        
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"
        
        items_count = cart_page.get_cart_items_count()
        assert items_count == 2, "Cart should have 2 items"
        
        logger.info("Test passed: Cart with items viewed successfully")
    
    def test_cart_displays_correct_item_names(self, logged_in_driver_with_cart_items):
        """Test that cart displays correct item names"""
        logger.info("Starting test: Cart displays correct item names")
        
        driver = logged_in_driver_with_cart_items
        products_page = ProductsPage(driver)
        
        products_page.go_to_cart()
        cart_page = CartPage(driver)
        
        cart_item_names = cart_page.get_cart_item_names()
        assert len(cart_item_names) == 2, "Should have 2 items in cart"
        assert all(name for name in cart_item_names), "All items should have names"
        
        logger.info(f"Test passed: Cart items: {cart_item_names}")
    
    def test_remove_item_from_cart(self, logged_in_driver_with_cart_items):
        """Test removing item from cart"""
        logger.info("Starting test: Remove item from cart")
        
        driver = logged_in_driver_with_cart_items
        products_page = ProductsPage(driver)
        
        products_page.go_to_cart()
        cart_page = CartPage(driver)
        
        initial_count = cart_page.get_cart_items_count()
        assert initial_count == 2, "Cart should have 2 items"
        
        cart_page.remove_item_from_cart(0)
        
        final_count = cart_page.get_cart_items_count()
        assert final_count == 1, "Cart should have 1 item after removal"
        
        logger.info("Test passed: Item removed from cart successfully")
    
    def test_continue_shopping_from_cart(self, logged_in_driver_with_cart_items):
        """Test continuing shopping from cart"""
        logger.info("Starting test: Continue shopping from cart")
        
        driver = logged_in_driver_with_cart_items
        products_page = ProductsPage(driver)
        
        products_page.go_to_cart()
        cart_page = CartPage(driver)
        
        cart_page.continue_shopping()
        
        assert "inventory" in driver.current_url, "Should return to products page"
        
        logger.info("Test passed: Continued shopping successfully")


@pytest.mark.cart
@pytest.mark.negative
class TestCartPageNegative:
    """Negative test cases for cart functionality"""
    
    def test_empty_cart(self, driver):
        """Test viewing empty cart"""
        logger.info("Starting test: View empty cart")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        products_page = ProductsPage(driver)
        products_page.go_to_cart()
        
        cart_page = CartPage(driver)
        
        items_count = cart_page.get_cart_items_count()
        assert items_count == 0, "Cart should be empty"
        
        logger.info("Test passed: Empty cart displayed successfully")
    
    def test_remove_item_by_invalid_name(self, logged_in_driver_with_cart_items):
        """Test removing non-existent item from cart"""
        logger.info("Starting test: Remove invalid item from cart")
        
        driver = logged_in_driver_with_cart_items
        products_page = ProductsPage(driver)
        
        products_page.go_to_cart()
        cart_page = CartPage(driver)
        
        initial_count = cart_page.get_cart_items_count()
        
        cart_page.remove_item_from_cart_by_name("InvalidItem")
        
        final_count = cart_page.get_cart_items_count()
        assert final_count == initial_count, "Cart items should not change"
        
        logger.info("Test passed: Invalid item removal handled correctly")

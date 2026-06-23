import pytest
import logging
from config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

logger = logging.getLogger(__name__)


@pytest.fixture
def logged_in_driver(driver):
    """Fixture to provide a logged-in driver"""
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    return driver


@pytest.mark.product
@pytest.mark.positive
@pytest.mark.smoke
class TestProductsPagePositive:
    """Positive test cases for products page functionality"""
    
    def test_products_page_loads_successfully(self, logged_in_driver):
        """Test that products page loads after login"""
        logger.info("Starting test: Products page loads successfully")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        assert products_page.is_products_page_loaded(), "Products page not loaded"
        assert driver.current_url == f"{Config.BASE_URL}/inventory.html", "Incorrect URL"
        
        logger.info("Test passed: Products page loaded successfully")
    
    def test_products_displayed(self, logged_in_driver):
        """Test that products are displayed on page"""
        logger.info("Starting test: Products are displayed")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        count = products_page.get_products_count()
        assert count > 0, "No products displayed"
        
        names = products_page.get_product_names()
        assert len(names) == count, "Product names count mismatch"
        
        logger.info(f"Test passed: {count} products displayed")
    
    def test_add_single_product_to_cart(self, logged_in_driver):
        """Test adding single product to cart"""
        logger.info("Starting test: Add single product to cart")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_product_to_cart(0)
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == 1, "Cart count should be 1"
        
        logger.info("Test passed: Single product added to cart")
    
    def test_add_multiple_products_to_cart(self, logged_in_driver):
        """Test adding multiple products to cart"""
        logger.info("Starting test: Add multiple products to cart")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_product_to_cart(0)
        products_page.add_product_to_cart(1)
        products_page.add_product_to_cart(2)
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == 3, "Cart count should be 3"
        
        logger.info("Test passed: Multiple products added to cart")
    
    def test_add_product_by_name(self, logged_in_driver):
        """Test adding product by name"""
        logger.info("Starting test: Add product by name")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        names = products_page.get_product_names()
        first_product_name = names[0]
        
        products_page.add_product_to_cart_by_name(first_product_name)
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == 1, "Cart count should be 1"
        
        logger.info(f"Test passed: Product '{first_product_name}' added to cart")


@pytest.mark.product
@pytest.mark.negative
class TestProductsPageNegative:
    """Negative test cases for products page functionality"""
    
    def test_add_nonexistent_product_to_cart(self, logged_in_driver):
        """Test adding non-existent product (should not crash)"""
        logger.info("Starting test: Add non-existent product to cart")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_product_to_cart_by_name("NonExistentProduct")
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == 0, "Cart should remain empty"
        
        logger.info("Test passed: Non-existent product not added to cart")
    
    def test_sort_products(self, logged_in_driver):
        """Test sorting products"""
        logger.info("Starting test: Sort products")
        
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        original_names = products_page.get_product_names()
        
        products_page.sort_products("za")
        
        sorted_names = products_page.get_product_names()
        assert sorted_names != original_names, "Product order should change after sorting"
        
        logger.info("Test passed: Products sorted successfully")

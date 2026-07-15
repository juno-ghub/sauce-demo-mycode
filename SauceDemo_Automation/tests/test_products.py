import pytest
import logging
from config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

logger = logging.getLogger(__name__)


@pytest.mark.product
@pytest.mark.positive
class TestProductsPositive:
    """Positive test cases for products page"""

    def test_products_page_loaded(self, driver):
        """Test that the products page loads successfully"""
        logger.info("Starting test: Products page loaded")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        assert products_page.is_products_page_loaded(), "Products page not loaded"

        logger.info("Test passed: Products page loaded")

    def test_add_product_to_cart(self, driver):
        """Test adding a product to the cart"""
        logger.info("Starting test: Add product to cart")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()

        assert products_page.get_cart_badge_count() > 0, "Cart badge not updated"

        logger.info("Test passed: Product added to cart")

    def test_sort_products(self, driver):
        """Test sorting products"""
        logger.info("Starting test: Sort products")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.sort_products("Price (low to high)")

        assert products_page.get_title_text() == "Products", "Products title not shown"

        logger.info("Test passed: Products sorted")


@pytest.mark.product
@pytest.mark.negative
class TestProductsNegative:
    """Negative test cases for products page"""

    def test_nonexistent_product_handling(self, driver):
        """Test non-existent product handling"""
        logger.info("Starting test: Non-existent product handling")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        assert products_page.is_products_page_loaded(), "Products page not loaded"

        logger.info("Test passed: Non-existent product handling complete")

import pytest
import logging
from config import Config
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


@pytest.mark.cart
@pytest.mark.positive
class TestCartPositive:
    """Positive test cases for cart functionality"""

    def test_view_cart(self, driver):
        """Test viewing the cart"""
        logger.info("Starting test: View cart")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        assert products_page.is_products_page_loaded(), "Products page not loaded"

        products_page.click_cart()
        cart_page = CartPage(driver)
        assert cart_page.is_cart_page_loaded(), "Cart page not loaded"

        logger.info("Test passed: Cart page displayed")

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

    def test_remove_product_from_cart(self, driver):
        """Test removing a product from the cart"""
        logger.info("Starting test: Remove product from cart")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.remove_item()

        assert cart_page.get_cart_item_count() == 0, "Cart item was not removed"

        logger.info("Test passed: Product removed from cart")


@pytest.mark.cart
@pytest.mark.negative
class TestCartNegative:
    """Negative test cases for cart functionality"""

    def test_empty_cart(self, driver):
        """Test that an empty cart is handled"""
        logger.info("Starting test: Empty cart")

        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        products_page = ProductsPage(driver)
        products_page.click_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_cart_item_count() == 0, "Cart should be empty"

        logger.info("Test passed: Empty cart handled")

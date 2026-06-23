from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class ProductsPage(BasePage):
    """Products page object for saucedemo.com"""
    
    # Locators
    PRODUCTS_CONTAINER = (By.CLASS_NAME, "inventory_container")
    PRODUCT_ITEM = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    SIDEBAR_MENU = (By.CLASS_NAME, "bm-menu")
    
    def __init__(self, driver):
        super().__init__(driver)
        logger.info("ProductsPage initialized")
    
    def is_products_page_loaded(self):
        """
        Check if products page is loaded
        
        Returns:
            Boolean
        """
        is_loaded = self.is_element_displayed(self.PRODUCTS_CONTAINER)
        logger.info(f"Products page loaded: {is_loaded}")
        return is_loaded
    
    def get_products_count(self):
        """
        Get total number of products displayed
        
        Returns:
            Number of products
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        count = len(products)
        logger.info(f"Total products: {count}")
        return count
    
    def get_product_names(self):
        """
        Get all product names
        
        Returns:
            List of product names
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        names = [product.find_element(*self.PRODUCT_NAME).text for product in products]
        logger.info(f"Product names: {names}")
        return names
    
    def add_product_to_cart(self, product_index=0):
        """
        Add product to cart by index
        
        Args:
            product_index: Index of product to add (default: 0)
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        if product_index < len(products):
            button = products[product_index].find_element(By.XPATH, ".//button[contains(@class, 'btn_inventory')]")
            button.click()
            logger.info(f"Added product at index {product_index} to cart")
        else:
            logger.error(f"Product index {product_index} out of range")
    
    def add_product_to_cart_by_name(self, product_name):
        """
        Add product to cart by name
        
        Args:
            product_name: Name of product to add
        """
        products = self.find_elements(self.PRODUCT_ITEM)
        for product in products:
            name_element = product.find_element(*self.PRODUCT_NAME)
            if name_element.text == product_name:
                button = product.find_element(By.XPATH, ".//button[contains(@class, 'btn_inventory')]")
                button.click()
                logger.info(f"Added product '{product_name}' to cart")
                return
        logger.warning(f"Product '{product_name}' not found")
    
    def get_cart_badge_count(self):
        """
        Get number of items in cart badge
        
        Returns:
            Number of items in cart
        """
        try:
            badge_text = self.get_text(self.CART_BADGE)
            count = int(badge_text)
            logger.info(f"Cart badge count: {count}")
            return count
        except:
            logger.info("Cart badge not found or empty")
            return 0
    
    def go_to_cart(self):
        """Click on cart link to go to cart page"""
        logger.info("Going to cart page")
        self.click_element(self.CART_LINK)
    
    def sort_products(self, sort_option):
        """
        Sort products by option
        
        Args:
            sort_option: Sort option value (e.g., 'az', 'za', 'lohi', 'hilo')
        """
        logger.info(f"Sorting products by: {sort_option}")
        self.click_element(self.SORT_DROPDOWN)
        self.click_element((By.XPATH, f"//option[@value='{sort_option}']"))
    
    def logout(self):
        """Logout from application"""
        logger.info("Logging out")
        self.click_element(self.HAMBURGER_MENU)
        self.click_element(self.LOGOUT_LINK)

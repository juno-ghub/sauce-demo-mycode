from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class CartPage(BasePage):
    """Cart page object for saucedemo.com"""
    
    # Locators
    CART_CONTAINER = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@class, 'btn_danger')]")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_EMPTY_MESSAGE = (By.CLASS_NAME, "complete-header")
    
    def __init__(self, driver):
        super().__init__(driver)
        logger.info("CartPage initialized")
    
    def is_cart_page_loaded(self):
        """
        Check if cart page is loaded
        
        Returns:
            Boolean
        """
        is_loaded = self.is_element_displayed(self.CART_CONTAINER)
        logger.info(f"Cart page loaded: {is_loaded}")
        return is_loaded
    
    def get_cart_items_count(self):
        """
        Get total number of items in cart
        
        Returns:
            Number of items in cart
        """
        items = self.find_elements(self.CART_ITEM)
        count = len(items)
        logger.info(f"Total items in cart: {count}")
        return count
    
    def get_cart_item_names(self):
        """
        Get all product names in cart
        
        Returns:
            List of product names
        """
        items = self.find_elements(self.CART_ITEM)
        names = [item.find_element(*self.CART_ITEM_NAME).text for item in items]
        logger.info(f"Cart item names: {names}")
        return names
    
    def get_cart_item_prices(self):
        """
        Get all product prices in cart
        
        Returns:
            List of product prices
        """
        items = self.find_elements(self.CART_ITEM)
        prices = [item.find_element(*self.CART_ITEM_PRICE).text for item in items]
        logger.info(f"Cart item prices: {prices}")
        return prices
    
    def remove_item_from_cart(self, item_index=0):
        """
        Remove item from cart by index
        
        Args:
            item_index: Index of item to remove (default: 0)
        """
        items = self.find_elements(self.CART_ITEM)
        if item_index < len(items):
            button = items[item_index].find_element(By.XPATH, ".//button[contains(@class, 'btn_danger')]")
            button.click()
            logger.info(f"Removed item at index {item_index} from cart")
        else:
            logger.error(f"Item index {item_index} out of range")
    
    def remove_item_from_cart_by_name(self, item_name):
        """
        Remove item from cart by name
        
        Args:
            item_name: Name of item to remove
        """
        items = self.find_elements(self.CART_ITEM)
        for item in items:
            name_element = item.find_element(*self.CART_ITEM_NAME)
            if name_element.text == item_name:
                button = item.find_element(By.XPATH, ".//button[contains(@class, 'btn_danger')]")
                button.click()
                logger.info(f"Removed item '{item_name}' from cart")
                return
        logger.warning(f"Item '{item_name}' not found in cart")
    
    def continue_shopping(self):
        """Click continue shopping button"""
        logger.info("Clicking continue shopping button")
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
    
    def proceed_to_checkout(self):
        """Click checkout button"""
        logger.info("Clicking checkout button")
        self.click_element(self.CHECKOUT_BUTTON)

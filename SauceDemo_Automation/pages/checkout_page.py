from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class CheckoutPage(BasePage):
    """Checkout page object for saucedemo.com"""
    
    # Locators - Checkout Step One
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    
    # Locators - Checkout Step Two
    CHECKOUT_SUMMARY = (By.CLASS_NAME, "summary_info")
    FINISH_BUTTON = (By.ID, "finish")
    
    # Locators - Order Confirmation
    ORDER_CONFIRMATION = (By.CLASS_NAME, "complete-header")
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def __init__(self, driver):
        super().__init__(driver)
        logger.info("CheckoutPage initialized")
    
    def enter_first_name(self, first_name):
        """
        Enter first name
        
        Args:
            first_name: First name to enter
        """
        logger.info(f"Entering first name: {first_name}")
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """
        Enter last name
        
        Args:
            last_name: Last name to enter
        """
        logger.info(f"Entering last name: {last_name}")
        self.send_keys(self.LAST_NAME_INPUT, last_name)
    
    def enter_postal_code(self, postal_code):
        """
        Enter postal code
        
        Args:
            postal_code: Postal code to enter
        """
        logger.info(f"Entering postal code: {postal_code}")
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
    
    def fill_checkout_information(self, first_name, last_name, postal_code):
        """
        Fill all checkout information
        
        Args:
            first_name: First name
            last_name: Last name
            postal_code: Postal code
        """
        logger.info("Filling checkout information")
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
    
    def click_continue(self):
        """Click continue button"""
        logger.info("Clicking continue button")
        self.click_element(self.CONTINUE_BUTTON)
    
    def click_finish(self):
        """Click finish button"""
        logger.info("Clicking finish button")
        self.click_element(self.FINISH_BUTTON)
    
    def get_error_message(self):
        """
        Get error message
        
        Returns:
            Error message text
        """
        error_text = self.get_text(self.ERROR_MESSAGE)
        logger.info(f"Error message: {error_text}")
        return error_text
    
    def is_error_message_displayed(self):
        """
        Check if error message is displayed
        
        Returns:
            Boolean
        """
        is_displayed = self.is_element_displayed(self.ERROR_MESSAGE)
        logger.info(f"Error message displayed: {is_displayed}")
        return is_displayed
    
    def is_order_confirmation_displayed(self):
        """
        Check if order confirmation is displayed
        
        Returns:
            Boolean
        """
        is_displayed = self.is_element_displayed(self.ORDER_CONFIRMATION)
        logger.info(f"Order confirmation displayed: {is_displayed}")
        return is_displayed
    
    def get_confirmation_message(self):
        """
        Get order confirmation message
        
        Returns:
            Confirmation message text
        """
        message = self.get_text(self.CONFIRMATION_MESSAGE)
        logger.info(f"Confirmation message: {message}")
        return message
    
    def click_back_to_home(self):
        """Click back to home button"""
        logger.info("Clicking back to home button")
        self.click_element(self.BACK_HOME_BUTTON)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Login page object for saucedemo.com"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    LOGIN_CONTAINER = (By.CLASS_NAME, "login_container")
    
    def __init__(self, driver):
        super().__init__(driver)
        logger.info("LoginPage initialized")
    
    def enter_username(self, username):
        """
        Enter username
        
        Args:
            username: Username to enter
        """
        logger.info(f"Entering username: {username}")
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """
        Enter password
        
        Args:
            password: Password to enter
        """
        logger.info(f"Entering password")
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click login button"""
        logger.info("Clicking login button")
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Perform login with username and password
        
        Args:
            username: Username
            password: Password
        """
        logger.info(f"Logging in with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """
        Get error message displayed on login page
        
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
    
    def is_login_page_loaded(self):
        """
        Check if login page is loaded
        
        Returns:
            Boolean
        """
        is_loaded = self.is_element_displayed(self.LOGIN_CONTAINER)
        logger.info(f"Login page loaded: {is_loaded}")
        return is_loaded

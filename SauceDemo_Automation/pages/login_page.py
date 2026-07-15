from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the SauceDemo login page."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_page_loaded(self):
        """Check if login page loaded successfully."""
        return self.driver.current_url.endswith("/") or "saucedemo" in self.driver.current_url

    def login(self, username, password):
        """Login with the provided credentials."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def enter_username(self, username):
        """Enter username."""
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password."""
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click login button."""
        self.click(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        """Check if an error message is displayed."""
        return self.is_element_displayed(self.ERROR_MESSAGE)

    def get_error_message(self):
        """Get the error message text."""
        return self.get_text(self.ERROR_MESSAGE)

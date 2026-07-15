from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for the checkout page."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        """Enter the first name."""
        self.type(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        """Enter the last name."""
        self.type(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        """Enter the postal code."""
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        """Click the continue button."""
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        """Click the finish button."""
        self.click(self.FINISH_BUTTON)

    def is_error_message_displayed(self):
        """Check if an error message is displayed."""
        return self.is_element_displayed(self.ERROR_MESSAGE)

    def get_error_message(self):
        """Get the error message text."""
        return self.get_text(self.ERROR_MESSAGE)

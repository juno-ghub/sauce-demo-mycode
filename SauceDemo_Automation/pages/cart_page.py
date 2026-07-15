from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the cart page."""

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_page_loaded(self):
        """Check if cart page is loaded."""
        return "cart" in self.driver.current_url

    def get_cart_item_count(self):
        """Get the number of items in the cart."""
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_item(self):
        """Remove an item from the cart."""
        self.click(self.REMOVE_BUTTONS)

    def click_checkout(self):
        """Click the checkout button."""
        self.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        """Click the continue shopping button."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)

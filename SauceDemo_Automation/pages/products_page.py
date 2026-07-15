from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page object for the products page."""

    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        super().__init__(driver)

    def is_products_page_loaded(self):
        """Check if products page is loaded."""
        return "inventory" in self.driver.current_url

    def add_first_product_to_cart(self):
        """Add the first product to the cart."""
        self.click(self.ADD_TO_CART_BUTTONS)

    def get_products_count(self):
        """Get the number of products displayed."""
        return len(self.driver.find_elements(*self.INVENTORY_LIST))

    def get_cart_badge_count(self):
        """Get the cart badge count."""
        return int(self.driver.find_element(*self.CART_BADGE).text) if self.is_element_displayed(self.CART_BADGE) else 0

    def sort_products(self, option):
        """Sort products by the provided option."""
        self.driver.find_element(*self.SORT_DROPDOWN).click()
        self.driver.find_element(By.XPATH, f"//option[.='{option}']").click()

    def click_cart(self):
        """Click the cart icon."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def get_title_text(self):
        """Get the title text."""
        return self.get_text(self.TITLE)

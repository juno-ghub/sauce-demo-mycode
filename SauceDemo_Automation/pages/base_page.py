from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base class with common Selenium methods used by all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator, timeout=10):
        """Find an element and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Click an element."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        """Type text into an input field."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_displayed(self, locator):
        """Check if an element is displayed."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def get_text(self, locator):
        """Get the text of an element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_title(self):
        """Get the page title."""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL."""
        return self.driver.current_url

    def scroll_to_element(self, locator):
        """Scroll to an element."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_url_contains(self, text, timeout=10):
        """Wait for the URL to contain a specific text."""
        self.wait.until(EC.url_contains(text))

    def take_screenshot(self, name):
        """Take a screenshot and save it to the screenshots directory."""
        screenshot_path = Path("screenshots") / f"{name}.png"
        screenshot_path.parent.mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(str(screenshot_path))
        logger.info(f"Screenshot saved to {screenshot_path}")


class PageObjectError(Exception):
    """Custom exception for page object errors."""
    pass

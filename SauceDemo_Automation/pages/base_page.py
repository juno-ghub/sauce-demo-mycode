import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import Config

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class containing common methods for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator):
        """
        Find element by locator with explicit wait
        
        Args:
            locator: Tuple of (By, value)
        
        Returns:
            WebElement
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logger.debug(f"Found element: {locator}")
            return element
        except Exception as e:
            logger.error(f"Failed to find element {locator}: {str(e)}")
            raise
    
    def find_elements(self, locator):
        """
        Find multiple elements by locator
        
        Args:
            locator: Tuple of (By, value)
        
        Returns:
            List of WebElements
        """
        try:
            elements = self.driver.find_elements(*locator)
            logger.debug(f"Found {len(elements)} elements: {locator}")
            return elements
        except Exception as e:
            logger.error(f"Failed to find elements {locator}: {str(e)}")
            raise
    
    def click_element(self, locator):
        """
        Click on element
        
        Args:
            locator: Tuple of (By, value)
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Clicked element: {locator}")
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {str(e)}")
            raise
    
    def send_keys(self, locator, text):
        """
        Send keys to element
        
        Args:
            locator: Tuple of (By, value)
            text: Text to send
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            logger.info(f"Sent keys to element {locator}: {text}")
        except Exception as e:
            logger.error(f"Failed to send keys to element {locator}: {str(e)}")
            raise
    
    def get_text(self, locator):
        """
        Get text from element
        
        Args:
            locator: Tuple of (By, value)
        
        Returns:
            Text content of element
        """
        try:
            element = self.find_element(locator)
            text = element.text
            logger.debug(f"Got text from element {locator}: {text}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text from element {locator}: {str(e)}")
            raise
    
    def is_element_displayed(self, locator):
        """
        Check if element is displayed
        
        Args:
            locator: Tuple of (By, value)
        
        Returns:
            Boolean
        """
        try:
            element = self.driver.find_elements(*locator)
            if element:
                return element[0].is_displayed()
            return False
        except Exception as e:
            logger.error(f"Failed to check if element is displayed {locator}: {str(e)}")
            return False
    
    def wait_for_element_visibility(self, locator):
        """
        Wait for element to be visible
        
        Args:
            locator: Tuple of (By, value)
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            logger.debug(f"Element is visible: {locator}")
        except Exception as e:
            logger.error(f"Element not visible {locator}: {str(e)}")
            raise
    
    def get_current_url(self):
        """Get current URL"""
        url = self.driver.current_url
        logger.debug(f"Current URL: {url}")
        return url
    
    def navigate_to(self, url):
        """Navigate to URL"""
        self.driver.get(url)
        logger.info(f"Navigated to: {url}")
    
    def get_title(self):
        """Get page title"""
        title = self.driver.title
        logger.debug(f"Page title: {title}")
        return title
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.info(f"Scrolled to element: {locator}")
        except Exception as e:
            logger.error(f"Failed to scroll to element {locator}: {str(e)}")
            raise
    
    def hover_over_element(self, locator):
        """Hover over element"""
        try:
            element = self.find_element(locator)
            self.actions.move_to_element(element).perform()
            logger.info(f"Hovered over element: {locator}")
        except Exception as e:
            logger.error(f"Failed to hover over element {locator}: {str(e)}")
            raise

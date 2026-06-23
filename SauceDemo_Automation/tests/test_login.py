import pytest
import logging
from config import Config
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


@pytest.mark.login
@pytest.mark.positive
@pytest.mark.smoke
class TestLoginPositive:
    """Positive test cases for login functionality"""
    
    def test_login_with_valid_credentials(self, driver):
        """Test login with valid credentials"""
        logger.info("Starting test: Login with valid credentials")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        
        assert login_page.is_login_page_loaded(), "Login page not loaded"
        
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        
        # Wait for redirect to products page
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        
        assert "inventory" in driver.current_url, "Did not redirect to products page"
        logger.info("Test passed: Successfully logged in with valid credentials")
    
    def test_login_page_elements_displayed(self, driver):
        """Test that all login page elements are displayed"""
        logger.info("Starting test: Login page elements displayed")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        
        assert login_page.is_login_page_loaded(), "Login page not loaded"
        assert login_page.is_element_displayed(login_page.USERNAME_INPUT), "Username input not displayed"
        assert login_page.is_element_displayed(login_page.PASSWORD_INPUT), "Password input not displayed"
        assert login_page.is_element_displayed(login_page.LOGIN_BUTTON), "Login button not displayed"
        
        logger.info("Test passed: All login page elements are displayed")


@pytest.mark.login
@pytest.mark.negative
class TestLoginNegative:
    """Negative test cases for login functionality"""
    
    def test_login_with_invalid_credentials(self, driver):
        """Test login with invalid credentials"""
        logger.info("Starting test: Login with invalid credentials")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        
        login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
        
        assert login_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = login_page.get_error_message()
        assert "Username and password" in error_msg, "Invalid error message"
        
        logger.info("Test passed: Error message displayed for invalid credentials")
    
    def test_login_with_locked_out_user(self, driver):
        """Test login with locked out user"""
        logger.info("Starting test: Login with locked out user")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        
        login_page.login(Config.LOCKED_USERNAME, Config.VALID_PASSWORD)
        
        assert login_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg, "Locked out error message not shown"
        
        logger.info("Test passed: Locked out user cannot login")
    
    def test_login_with_empty_username(self, driver):
        """Test login with empty username"""
        logger.info("Starting test: Login with empty username")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        
        login_page.enter_password(Config.VALID_PASSWORD)
        login_page.click_login_button()
        
        assert login_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = login_page.get_error_message()
        assert "Username is required" in error_msg, "Username required error not shown"
        
        logger.info("Test passed: Error message displayed for empty username")
    
    def test_login_with_empty_password(self, driver):
        """Test login with empty password"""
        logger.info("Starting test: Login with empty password")
        
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        
        login_page.enter_username(Config.VALID_USERNAME)
        login_page.click_login_button()
        
        assert login_page.is_error_message_displayed(), "Error message not displayed"
        error_msg = login_page.get_error_message()
        assert "Password is required" in error_msg, "Password required error not shown"
        
        logger.info("Test passed: Error message displayed for empty password")

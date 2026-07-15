import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import Config

# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def setup_directories():
    """Create required directories if they don't exist"""
    directories = [Config.SCREENSHOT_PATH, Config.REPORTS_PATH, Config.ALLURE_RESULTS_PATH]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        logger.info(f"Directory ensured: {directory}")


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to initialize and tear down the WebDriver
    """
    logger.info("Initializing WebDriver")
    
    if Config.BROWSER.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        
        # Disable password manager and save password popups
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_leak_detection": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_settings.popups": 0
        })
        
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif Config.BROWSER.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        # Disable password manager prompts
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("signon.autofillForms", False)
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.maximize_window()
    
    logger.info(f"WebDriver initialized: {Config.BROWSER}")
    
    yield driver
    
    # Teardown
    logger.info("Closing WebDriver")
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def test_logger():
    """Provide logger for each test"""
    return logger


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs.get("driver")
            if driver:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{item.name}_{timestamp}.png"
                filepath = os.path.join(Config.SCREENSHOT_PATH, filename)
                try:
                    driver.save_screenshot(filepath)
                    logger.error(f"Screenshot saved: {filepath}")
                except Exception as e:
                    logger.error(f"Failed to save screenshot: {str(e)}")

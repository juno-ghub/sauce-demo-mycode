import os
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path
from config import Config


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Create and return a WebDriver instance for each test."""
    browser = Config.BROWSER.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshots on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = Path(Config.SCREENSHOT_PATH)
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshot_dir / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))
            logger.info(f"Screenshot saved to {screenshot_path}")


@pytest.fixture(autouse=True)
def setup_directories():
    """Create screenshot and report directories if they don't exist."""
    for path in [Config.SCREENSHOT_PATH, Config.REPORT_PATH, Config.ALLURE_RESULTS_PATH]:
        Path(path).mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="function")
def webdriver_wait(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, Config.EXPLICIT_WAIT)

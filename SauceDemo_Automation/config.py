import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for Selenium automation framework"""
    
    # Base URL
    BASE_URL = "https://www.saucedemo.com"
    
    # Browser settings
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))
    
    # Test users
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    LOCKED_USERNAME = "locked_out_user"
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_password"
    
    # Screenshots
    SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "screenshots")
    
    # Reports
    REPORTS_PATH = os.path.join(os.path.dirname(__file__), "reports")
    ALLURE_RESULTS_PATH = os.path.join(os.path.dirname(__file__), "allure-results")
    
    # Log settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

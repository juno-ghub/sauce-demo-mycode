import os
from pathlib import Path


class Config:
    BASE_URL = "https://www.saucedemo.com"
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_password"
    LOCKED_USERNAME = "locked_out_user"

    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 10

    SCREENSHOT_PATH = str(Path(__file__).parent / "screenshots")
    REPORT_PATH = str(Path(__file__).parent / "reports")
    ALLURE_RESULTS_PATH = str(Path(__file__).parent / "allure-results")

    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

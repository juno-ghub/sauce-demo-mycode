# SauceDemo Automation Framework

A comprehensive Selenium Python automation framework for testing the SauceDemo web application (https://www.saucedemo.com) using the Page Object Model (POM) pattern with pytest and Allure reporting.

## Project Structure

```
SauceDemo_Automation/
├── pages/                    # Page Object Model classes
│   ├── base_page.py         # Base page with common methods
│   ├── login_page.py        # Login page object
│   ├── products_page.py     # Products page object
│   ├── cart_page.py         # Cart page object
│   └── checkout_page.py     # Checkout page object
├── tests/                    # Test files
│   ├── test_login.py        # Login test scenarios
│   ├── test_products.py     # Product page test scenarios
│   ├── test_cart.py         # Cart functionality tests
│   └── test_checkout.py     # Checkout flow tests
├── screenshots/             # Test failure screenshots
├── reports/                 # HTML test reports
├── allure-results/          # Allure test results
├── config.py               # Configuration settings
├── conftest.py             # Pytest fixtures and hooks
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Chrome or Firefox browser

## Installation

1. **Clone or download the project:**
   ```bash
   cd C:\Users\JaelN\SauceDemo_Automation
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.py` to modify:
- Base URL
- Browser type (chrome/firefox)
- Headless mode
- Wait times (implicit/explicit)
- Test credentials
- Screenshot and report paths

## Test Credentials (SauceDemo)

- **Valid User:** standard_user / secret_sauce
- **Locked User:** locked_out_user / secret_sauce
- **Invalid Credentials:** Any other combination

## Running Tests

### Run all tests:
```bash
pytest
```

### Run tests with specific marker:
```bash
pytest -m smoke
pytest -m login
pytest -m positive
pytest -m negative
```

### Run tests in specific file:
```bash
pytest tests/test_login.py
```

### Run with verbose output:
```bash
pytest -v
```

### Run with HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run with Allure report:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### Run in parallel (requires pytest-xdist):
```bash
pytest -n 4
```

### Run with specific browser (set environment variable):
```bash
set BROWSER=firefox
pytest
```

### Run headless mode:
```bash
set HEADLESS=True
pytest
```

## Test Markers

- `@pytest.mark.smoke` - Smoke tests
- `@pytest.mark.sanity` - Sanity tests
- `@pytest.mark.regression` - Regression tests
- `@pytest.mark.positive` - Positive test cases
- `@pytest.mark.negative` - Negative test cases
- `@pytest.mark.login` - Login tests
- `@pytest.mark.product` - Product tests
- `@pytest.mark.cart` - Cart tests
- `@pytest.mark.checkout` - Checkout tests

## Test Coverage

### Login Tests (test_login.py)
- **Positive:** Valid login, page elements verification
- **Negative:** Invalid credentials, locked user, empty fields

### Product Tests (test_products.py)
- **Positive:** Page load, products display, add to cart, multiple products, sort
- **Negative:** Non-existent product handling

### Cart Tests (test_cart.py)
- **Positive:** View cart, display items, remove items, continue shopping
- **Negative:** Empty cart, invalid item removal

### Checkout Tests (test_checkout.py)
- **Positive:** Complete checkout flow, valid information
- **Negative:** Missing first name, last name, postal code

## Features

### Page Object Model
- Centralized element locators
- Reusable page methods
- Separation of concerns

### Base Page
- Common methods for all pages (find_element, click, send_keys, etc.)
- Explicit waits using WebDriverWait
- Error logging and handling

### Fixtures
- Automatic WebDriver initialization
- Browser configuration
- Automatic screenshot on failure
- Directory setup

### Logging
- Comprehensive logging throughout tests
- Log level configuration
- Test execution tracking

### Reporting
- HTML reports with pytest-html
- Allure test reports with detailed metrics
- Automatic screenshots on test failure

## Troubleshooting

### WebDriver Not Found
- Ensure webdriver-manager is installed
- Check browser is installed and accessible
- Clear WebDriver cache: `pip install --upgrade webdriver-manager`

### Tests Not Running
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check pytest is installed: `pytest --version`
- Verify test files are in tests/ directory

### Screenshots Not Saved
- Ensure screenshots/ directory exists
- Check file permissions
- Verify SCREENSHOT_PATH in config.py

### Allure Report Not Generating
- Install Allure: Download from https://docs.qameta.io/allure/
- Add Allure to PATH
- Run: `allure serve allure-results`

## Best Practices Used

1. **POM Pattern** - Separates test logic from page elements
2. **Fixtures** - Reusable test setup and teardown
3. **Explicit Waits** - Prevents timing issues
4. **Logging** - Better debugging and monitoring
5. **Markers** - Organized test execution
6. **Configuration** - Centralized settings management
7. **Error Handling** - Comprehensive exception handling
8. **Documentation** - Clear code comments and docstrings

## Dependencies

- **selenium** - Web browser automation
- **pytest** - Testing framework
- **pytest-html** - HTML report generation
- **pytest-xdist** - Parallel execution
- **allure-pytest** - Allure report integration
- **python-dotenv** - Environment variable management
- **webdriver-manager** - Automatic WebDriver management
- **pillow** - Image handling for screenshots

## CI/CD Integration

For CI/CD pipelines, use:
```bash
pytest --alluredir=allure-results -v --tb=short
```

Then generate Allure report in your CI/CD system.

## Contributing

1. Follow POM pattern for new page objects
2. Use fixtures for test setup
3. Add appropriate markers to tests
4. Update this README with new test cases
5. Maintain consistent logging

## License

This project is provided as-is for testing purposes.

## Support

For issues or questions, refer to:
- Selenium Documentation: https://www.selenium.dev/documentation/
- Pytest Documentation: https://docs.pytest.org/
- Allure Documentation: https://docs.qameta.io/allure/

---

**Created:** 2024
**Framework Version:** 1.0

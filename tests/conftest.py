import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Global driver reference for manual control
_driver = None

def get_global_driver():
    global _driver
    return _driver

@pytest.fixture(scope="session")
def driver():
    global _driver
    if _driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--log-level=3")  # Fatal errors only
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable DevTools logging
        chrome_options.add_experimental_option('detach', True)  # Keep browser open after tests
        _driver = webdriver.Chrome(options=chrome_options)
    yield _driver
    # Do not quit here; let the runner handle quitting after Enter is pressed

@pytest.fixture(scope="session")
def config():
    from utilities.config_reader import get_config
    return get_config()['dev']

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = None
        # Try to get driver from fixture
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
        else:
            # Try global driver
            from tests.conftest import get_global_driver
            driver = get_global_driver()
        if driver:
            from utilities.screenshot import take_screenshot
            test_name = item.name.replace(' ', '_')
            take_screenshot(driver, name=f"FAIL_{test_name}")
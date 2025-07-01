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
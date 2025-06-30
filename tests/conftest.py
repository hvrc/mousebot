import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--log-level=3")  # Fatal errors only
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable DevTools logging
    chrome_options.add_experimental_option('detach', True)  # Keep browser open after tests
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    from utilities.config_reader import get_config
    return get_config()['dev']

@pytest.fixture(autouse=True)
def test_completion(request):
    test_name = request.node.name
    print(f"\nRunning {test_name}...")
    yield
    next_item = request.node.nextitem
    next_test = f"start {next_item.name}" if next_item else "finish"
    input(f"{test_name} completed. Press Enter to {next_test}...")
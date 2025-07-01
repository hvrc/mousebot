import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import glob
from utilities.logger import TestLogger
import traceback

# Global driver reference for manual control
_driver = None

# Store the current suite report folder
_suite_report_folder = None
_suite_logger = None

def get_next_suite_report_folder():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../reports'))
    os.makedirs(base_dir, exist_ok=True)
    existing = glob.glob(os.path.join(base_dir, 'test_report_*'))
    nums = [int(os.path.basename(f).split('_')[-1]) for f in existing if os.path.basename(f).split('_')[-1].isdigit()]
    n = max(nums) + 1 if nums else 1
    folder = os.path.join(base_dir, f'test_report_{n}')
    os.makedirs(folder, exist_ok=True)
    return folder

def get_global_driver():
    global _driver
    return _driver

@pytest.fixture(scope="session")
def suite_report_folder():
    global _suite_report_folder
    if _suite_report_folder is None:
        _suite_report_folder = get_next_suite_report_folder()
    return _suite_report_folder

@pytest.fixture(scope="session")
def suite_logger(suite_report_folder):
    global _suite_logger
    if _suite_logger is None:
        _suite_logger = TestLogger(suite_report_folder, "TEST SUITE")
    return _suite_logger

@pytest.fixture(scope="session")
def driver():
    global _driver
    if _driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('detach', True)
        _driver = webdriver.Chrome(options=chrome_options)
    def fin():
        if _driver:
            try:
                _driver.quit()
                print("Browser closed.")
            except Exception:
                pass
    import pytest
    pytest.request = locals().get('request', None)
    if pytest.request:
        pytest.request.addfinalizer(fin)
    else:
        import atexit
        atexit.register(fin)
    yield _driver

@pytest.fixture(scope="function", autouse=True)
def test_artifacts(request, suite_report_folder, suite_logger):
    # Attach report folder and logger to node for use in hooks
    request.node._report_folder = suite_report_folder
    request.node._logger = suite_logger
    test_name = request.node.name.replace(' ', '_')
    suite_logger.log(f"[START] {test_name}")
    yield
    outcome = getattr(request.node, 'rep_call', None)
    status = 'PASS' if outcome and outcome.passed else 'FAIL'
    suite_logger.log(f"[END] {test_name} - STATUS: {status}")

@pytest.fixture(scope="session")
def config():
    from utilities.config_reader import get_config
    return get_config()['dev']

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        item.rep_call = rep
        if rep.failed:
            driver = None
            if 'driver' in item.fixturenames:
                driver = item.funcargs['driver']
            else:
                from tests.conftest import get_global_driver
                driver = get_global_driver()
            if driver:
                from utilities.screenshot import take_screenshot
                report_folder = getattr(item, '_report_folder', None)
                test_name = item.name.replace(' ', '_')
                if report_folder:
                    take_screenshot(driver, output_dir=report_folder, name=f"{test_name}")
                else:
                    take_screenshot(driver, output_dir='reports', name=f"{test_name}")
            logger = getattr(item, '_logger', None)
            if logger:
                logger.log(f"Test failed: {item.name}")
                # Log full exception info and traceback
                if call.excinfo:
                    exc_type = call.excinfo.type.__name__
                    exc_msg = str(call.excinfo.value)
                    tb_str = ''.join(traceback.format_exception(call.excinfo.type, call.excinfo.value, call.excinfo.tb))
                    logger.log(f"Exception type: {exc_type}")
                    logger.log(f"Exception message: {exc_msg}")
                    logger.log(f"Traceback:\n{tb_str}")
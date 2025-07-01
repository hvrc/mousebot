import pytest
from pages.import_page import ImportPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from utilities.screenshot import take_screenshot

def test_import_001(driver, config, request):
    import_page = ImportPage(driver)
    assert "homepage" in driver.current_url.lower() or "home" in driver.current_url.lower()
    # Use report folder for screenshots if needed
    report_folder = getattr(request.node, '_report_folder', 'reports')
    import_page.go_to_import(report_folder=report_folder)
    import_page.assert_on_import_page()

    # Wait for file input to be present (robust check for import page loaded)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "file-upload"))
        )
    except Exception:
        take_screenshot(driver, output_dir=report_folder, name="test_import_001_import_page_not_loaded")
        pytest.fail(f"Import page not loaded. Current URL: {driver.current_url}")

    # Upload the file directly to the hidden input
    data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/valid_data.xlsx'))
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys(data_file)

    # Click the Check for Errors button
    import_page.check_errors()

    # Wait for and click the Proceed with Import button
    try:
        proceed_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.proceed"))
        )
        proceed_btn.click()
    except Exception:
        take_screenshot(driver, output_dir=report_folder, name="test_import_001_proceed_not_found")
        pytest.fail("Proceed with Import button not found or not clickable.")

    # Wait for and click the Confirm Import button
    try:
        confirm_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.import"))
        )
        confirm_btn.click()
    except Exception:
        take_screenshot(driver, output_dir=report_folder, name="test_import_001_confirm_not_found")
        pytest.fail("Confirm Import button not found or not clickable.")

    # Close the import tab and switch back to the original tab
    try:
        current_handle = driver.current_window_handle
        all_handles = driver.window_handles
        # Assume the first handle is the original tab
        original_handle = all_handles[0]
        driver.close()  # Close the current (import) tab
        driver.switch_to.window(original_handle)
    except Exception:
        take_screenshot(driver, output_dir=report_folder, name="test_import_001_tab_switch_failed")
        pytest.fail("Failed to close import tab and switch back to original tab.")

    # Assert we are back on the home page
    assert "homepage.do" in driver.current_url.lower()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

# import tool page
class ImportPage(BasePage):
    CHECK_ERRORS_BTN = (By.XPATH, "//button[contains(@class, 'process')]")
    FILE_INPUT = (By.ID, "file-upload")
    PROCEED_BTN = (By.CSS_SELECTOR, "button.proceed")
    CONFIRM_BTN = (By.CSS_SELECTOR, "button.import")

    # check if on import page
    def assert_on_import_page(self):
        assert "import" in self.driver.current_url.lower() or "import" in self.driver.title.lower()
    
    # upload file to import
    def upload_file(self, file_path):
        wait = WebDriverWait(self.driver, 10)
        file_input = wait.until(EC.presence_of_element_located(self.FILE_INPUT))
        file_input.send_keys(file_path)
        time.sleep(1)

    # click check for errors button
    def check_errors(self):
        wait = WebDriverWait(self.driver, 10)
        check_errors_btn = wait.until(EC.element_to_be_clickable(self.CHECK_ERRORS_BTN))
        check_errors_btn.click()
        time.sleep(1)

    # proceed with import button
    def proceed_with_import(self):
        wait = WebDriverWait(self.driver, 10)
        proceed_btn = wait.until(EC.element_to_be_clickable(self.PROCEED_BTN))
        proceed_btn.click()
        time.sleep(1)

    # confirm import button
    def confirm_import(self):
        wait = WebDriverWait(self.driver, 10)
        confirm_btn = wait.until(EC.element_to_be_clickable(self.CONFIRM_BTN))
        confirm_btn.click()
        time.sleep(1)

    # close import tool tab and go back to original tab
    def close_import_tab_and_return(self):
        all_handles = self.driver.window_handles
        original_handle = all_handles[0]
        self.driver.close()
        self.driver.switch_to.window(original_handle)
        time.sleep(1)

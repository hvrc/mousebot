from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ImportPage(BasePage):
    IMPORT_CARD = (By.XPATH, "//p[text()='Import']/ancestor::div[contains(@class, 'MuiPaper-root')]")
    CHECK_ERRORS_BTN = (By.XPATH, "//button[contains(@class, 'process')]")
    FILE_INPUT = (By.ID, "file-upload")
    PROCEED_BTN = (By.CSS_SELECTOR, "button.proceed")
    CONFIRM_BTN = (By.CSS_SELECTOR, "button.import")

    def go_to_import(self, report_folder=None):
        wait = WebDriverWait(self.driver, 20)
        original_windows = self.driver.window_handles
        import_card = wait.until(EC.element_to_be_clickable(self.IMPORT_CARD))
        import_card.click()
        wait.until(lambda d: len(d.window_handles) > len(original_windows))
        new_windows = self.driver.window_handles
        new_tab = [w for w in new_windows if w not in original_windows][0]
        self.driver.switch_to.window(new_tab)
        wait.until(lambda driver: "import" in driver.current_url.lower() or driver.find_elements(*self.FILE_INPUT))
        time.sleep(1)

    def assert_on_import_page(self):
        assert "import" in self.driver.current_url.lower() or "import" in self.driver.title.lower()

    def check_errors(self):
        wait = WebDriverWait(self.driver, 20)
        check_errors_btn = wait.until(EC.element_to_be_clickable(self.CHECK_ERRORS_BTN))
        check_errors_btn.click()
        time.sleep(2)

    def upload_file(self, file_path, report_folder=None):
        wait = WebDriverWait(self.driver, 20)
        file_input = wait.until(EC.presence_of_element_located(self.FILE_INPUT))
        file_input.send_keys(file_path)
        time.sleep(1)

    def proceed_with_import(self, report_folder=None):
        wait = WebDriverWait(self.driver, 20)
        proceed_btn = wait.until(EC.element_to_be_clickable(self.PROCEED_BTN))
        proceed_btn.click()
        time.sleep(1)

    def confirm_import(self, report_folder=None):
        wait = WebDriverWait(self.driver, 20)
        confirm_btn = wait.until(EC.element_to_be_clickable(self.CONFIRM_BTN))
        confirm_btn.click()
        time.sleep(1)

    def close_import_tab_and_return(self, report_folder=None):
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        original_handle = all_handles[0]
        self.driver.close()
        self.driver.switch_to.window(original_handle)
        time.sleep(1)

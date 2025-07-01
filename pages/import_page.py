from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.screenshot import take_screenshot
from utilities.logger import TestLogger
import os

class ImportPage(BasePage):
    IMPORT_CARD = (By.XPATH, "//p[text()='Import']/ancestor::div[contains(@class, 'MuiPaper-root')]")
    CHECK_ERRORS_BTN = (By.XPATH, "//button[contains(@class, 'process')]")
    FILE_INPUT = (By.ID, "file-upload")

    def go_to_import(self, report_folder=None, logger=None):
        wait = WebDriverWait(self.driver, 20)
        try:
            original_windows = self.driver.window_handles
            import_card = wait.until(EC.element_to_be_clickable(self.IMPORT_CARD))
            import_card.click()
            # Wait for a new window/tab to open
            wait.until(lambda d: len(d.window_handles) > len(original_windows))
            new_windows = self.driver.window_handles
            new_tab = [w for w in new_windows if w not in original_windows][0]
            self.driver.switch_to.window(new_tab)
            # Wait for either URL to contain 'import' or file input to be present
            wait.until(lambda driver: "import" in driver.current_url.lower() or driver.find_elements(*self.FILE_INPUT))
            time.sleep(1)
        except Exception as e:
            if report_folder:
                take_screenshot(self.driver, output_dir=report_folder, name="go_to_import_failed")
            if logger:
                logger.log(f"[ERROR] Failed to navigate to import page: {e}. Current URL: {self.driver.current_url}")
            raise

    def assert_on_import_page(self):
        assert "import" in self.driver.current_url.lower() or "import" in self.driver.title.lower()

    def check_errors(self):
        wait = WebDriverWait(self.driver, 20)
        check_errors_btn = wait.until(EC.element_to_be_clickable(self.CHECK_ERRORS_BTN))
        check_errors_btn.click()
        time.sleep(2)

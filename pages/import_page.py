from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ImportPage(BasePage):
    IMPORT_CARD = (By.XPATH, "//p[text()='Import']/ancestor::div[contains(@class, 'MuiPaper-root')]")
    CHECK_ERRORS_BTN = (By.XPATH, "//button[contains(@class, 'process')]")

    def go_to_import(self):
        wait = WebDriverWait(self.driver, 20)
        import_card = wait.until(EC.element_to_be_clickable(self.IMPORT_CARD))
        import_card.click()
        wait.until(lambda driver: "import" in driver.current_url.lower() or driver.current_url.lower() != driver.current_url.lower())
        time.sleep(2)

    def assert_on_import_page(self):
        assert "import" in self.driver.current_url.lower() or "import" in self.driver.title.lower()

    def check_errors(self):
        wait = WebDriverWait(self.driver, 20)
        check_errors_btn = wait.until(EC.element_to_be_clickable(self.CHECK_ERRORS_BTN))
        check_errors_btn.click()
        time.sleep(2)

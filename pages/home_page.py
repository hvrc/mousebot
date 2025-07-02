import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

# at home page
# navigating to colony module
# this should have a method to go to the import tool
class HomePage(BasePage):
    MODULES_ICON = (By.ID, "apps-selected-open")
    COLONY_MODULE = (By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]")
    IMPORT_CARD = (By.XPATH, "//p[text()='Import']/ancestor::div[contains(@class, 'MuiPaper-root')]")
    FILE_INPUT = (By.ID, "file-upload")

    def go_to_colony(self):
        self.click_element(*self.MODULES_ICON)
        self.click_element(*self.COLONY_MODULE)

    def go_to_import(self):
        wait = WebDriverWait(self.driver, 10)
        original_windows = self.driver.window_handles
        import_card = wait.until(EC.element_to_be_clickable(self.IMPORT_CARD))
        import_card.click()
        wait.until(lambda d: len(d.window_handles) > len(original_windows))
        new_windows = self.driver.window_handles
        new_tab = [w for w in new_windows if w not in original_windows][0]
        self.driver.switch_to.window(new_tab)
        wait.until(lambda driver: "import" in driver.current_url.lower() or driver.find_elements(*self.FILE_INPUT))
        time.sleep(1)

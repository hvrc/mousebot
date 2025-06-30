from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    MODULES_ICON = (By.ID, "apps-selected-open")
    COLONY_MODULE = (By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]")

    def go_to_colony(self):
        self.click_element(*self.MODULES_ICON)
        self.click_element(*self.COLONY_MODULE)

from .base_page import BasePage
from selenium.webdriver.common.by import By

# at home page
# navigating to colony module
# this should have a method to go to the imprort tool
class HomePage(BasePage):
    MODULES_ICON = (By.ID, "apps-selected-open")
    COLONY_MODULE = (By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]")

    def go_to_colony(self):
        self.click_element(*self.MODULES_ICON)
        self.click_element(*self.COLONY_MODULE)

from .base_page import BasePage
from selenium.webdriver.common.by import By

# colony module page
# navigating to matings tab
# this should have methods to go to other tabs as well
class ColonyPage(BasePage):
    MATINGS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/mating/list.do')]")

    def go_to_matings(self):
        self.click_element(*self.MATINGS_TAB)

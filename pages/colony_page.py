from .base_page import BasePage
from selenium.webdriver.common.by import By

class ColonyPage(BasePage):
    MATINGS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/mating/list.do')]")

    def go_to_matings(self):
        self.click_element(*self.MATINGS_TAB)

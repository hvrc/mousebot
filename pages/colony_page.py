import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

# colony module page
# navigating to matings tab
# this should have methods to go to other tabs as well
class ColonyPage(BasePage):
    MATINGS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/mating/list.do')]")
    ANIMALS_TAB = (By.ID, "mice")
    HOME_BUTTON = (By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]")
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"
    STRAINS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/mouseline/list.do') and contains(@class, 'line textdecoration')]")

    def go_to_matings(self):
        self.click_element(*self.MATINGS_TAB)

    def go_to_animals_tab(self):
        self.click_element(*self.ANIMALS_TAB)
        time.sleep(1)

    def go_home(self):
        self.click_element(*self.HOME_BUTTON)
        time.sleep(1)

    def wait_for_empty_message(self, message):
        wait = WebDriverWait(self.driver, 10)
        xpath = self.EMPTY_MESSAGE_XPATH_TEMPLATE.format(message=message)
        empty_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        assert empty_message.is_displayed()
        time.sleep(1)

    def go_to_strains(self):
        if "smdb/mouseline/list.do" not in self.driver.current_url:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.STRAINS_TAB)
            ).click()
            time.sleep(1)

from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LittersPage(BasePage):
    FIRST_MATING_CHECKBOX = (By.CSS_SELECTOR, "#matinglist_table tbody tr[id] input.cbox")
    NEW_LITTER_BTN = (By.ID, "newLitter4MatingMenuButton")
    DOB_INPUT = (By.ID, "birthDatePicker")
    CREATE_LITTERS_BTN = (By.ID, "editSaveNewLitter")
    POPUP_OK_BTN = (By.XPATH, "//div[contains(@class, 'ui-dialog-buttonset')]/button/span[text()='OK']/..")
    HOME_BUTTON = (By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]")
    LITTERS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/litter/list.do')]")

    def select_first_mating(self):
        self.click_element(*self.FIRST_MATING_CHECKBOX)
        time.sleep(1)

    def click_new_litter(self):
        self.click_element(*self.NEW_LITTER_BTN)
        time.sleep(2)

    def enter_dob(self, dob):
        dob_input = self.find_element(*self.DOB_INPUT)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", dob_input)
        dob_input.clear()
        dob_input.send_keys(dob)
        time.sleep(1)

    def create_litters(self):
        self.click_element(*self.CREATE_LITTERS_BTN)
        time.sleep(1)

    def confirm_popup(self):
        self.click_element(*self.POPUP_OK_BTN)
        time.sleep(1)

    def go_home(self):
        self.click_element(*self.HOME_BUTTON)
        time.sleep(2)

    def go_to_litters_tab(self):
        self.click_element(*self.LITTERS_TAB)
        time.sleep(2)

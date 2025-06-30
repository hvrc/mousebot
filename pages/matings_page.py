from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class MatingsPage(BasePage):
    MATINGS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/mating/list.do')]")
    NEW_MATINGS_BTN = (By.ID, "newMatingMenuButton")
    FIRST_MALE_CHECKBOX = (By.CSS_SELECTOR, "table#malemouseTable tbody input.cbox[type='checkbox']:first-of-type")
    FIRST_FEMALE_CHECKBOX = (By.CSS_SELECTOR, "table#femalemouseTable tbody input.cbox[type='checkbox']:first-of-type")
    SETUP_DATE_INPUT = (By.ID, "setupDate")
    MATING_TAG = (By.ID, "matingTag")
    STRAIN_SELECT = (By.ID, "mouselineId")
    ADD_BTN = (By.ID, "batchApply")
    MOVE_BREEDERS_BTN = (By.ID, "submitBatchesAndMove")
    CREATE_UPDATE_CAGES_BTN = (By.ID, "moveApply")
    DONE_BTN = (By.ID, "backbtn")

    def go_to_matings_tab(self):
        self.click_element(*self.MATINGS_TAB)
        time.sleep(2)

    def start_new_mating(self):
        self.click_element(*self.NEW_MATINGS_BTN)
        time.sleep(2)

    def select_first_male(self):
        self.click_element(*self.FIRST_MALE_CHECKBOX)
        time.sleep(1)

    def select_first_female(self):
        self.click_element(*self.FIRST_FEMALE_CHECKBOX)
        time.sleep(1)

    def set_setup_date(self, date_str):
        date_input = self.find_element(*self.SETUP_DATE_INPUT)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_input)
        date_input.clear()
        date_input.send_keys(date_str)
        time.sleep(1)

    def set_mating_tag(self, tag):
        tag_input = self.find_element(*self.MATING_TAG)
        tag_input.clear()
        tag_input.send_keys(tag)
        time.sleep(1)

    def select_first_strain(self):
        strain_select = self.find_element(*self.STRAIN_SELECT)
        select = Select(strain_select)
        for option in select.options:
            if option.get_attribute("value"):
                select.select_by_value(option.get_attribute("value"))
                break
        time.sleep(1)

    def add_mating(self):
        self.click_element(*self.ADD_BTN)
        time.sleep(2)

    def move_breeders(self):
        self.click_element(*self.MOVE_BREEDERS_BTN)
        time.sleep(2)

    def create_update_cages(self):
        self.click_element(*self.CREATE_UPDATE_CAGES_BTN)
        time.sleep(2)

    def done(self):
        self.click_element(*self.DONE_BTN)
        time.sleep(2)

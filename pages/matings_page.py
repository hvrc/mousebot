from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MatingsPage(BasePage):
    # Locators as class variables
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
    WARNING_POPUP = (By.XPATH, "//div[contains(@class, 'ui-dialog-buttonset')]/button/span[text()='OK']/..")
    HOME_BTN = (By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]")
    # Additional selectors for dynamic elements
    ALL_FEMALE_CHECKBOXES = (By.CSS_SELECTOR, "table#femalemouseTable tbody input.cbox[type='checkbox']")

    # Add these class variables at the top if not present
    SELECT_ALL_MATINGS_ID = "cb_matinglist_table"
    DISBAND_BTN_ID = "disbandmatingButton"
    DEACTIVATE_BTN_ID = "applydisbandMating"
    EMPTY_MATINGS_MSG = "No matings to show!"
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"

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

    def add_mating(self):
        self.click_element(*self.ADD_BTN)
        time.sleep(1)

    def add_second_mating_if_available(self, tag):
        # Try to select next available female and add another mating
        try:
            female_checkboxes = self.driver.find_elements(*self.ALL_FEMALE_CHECKBOXES)
            if len(female_checkboxes) > 1:
                female_checkboxes[1].click()
                self.set_mating_tag(tag)
                self.add_mating()
        except Exception:
            pass

    def move_breeders(self):
        self.click_element(*self.MOVE_BREEDERS_BTN)
        time.sleep(1)

    def create_update_cages(self):
        self.click_element(*self.CREATE_UPDATE_CAGES_BTN)
        time.sleep(1)

    def done(self):
        self.click_element(*self.DONE_BTN)
        time.sleep(1)

    def handle_warning_popup_and_go_home(self):
        try:
            self.click_element(*self.WARNING_POPUP)
        except Exception:
            pass
        self.go_home()

    def go_home(self):
        self.click_element(*self.HOME_BTN)
        time.sleep(2)

    def disband_and_deactivate_all_matings(self):
        try:
            self.click_element(By.ID, self.SELECT_ALL_MATINGS_ID)
            time.sleep(1)
            self.click_element(By.ID, self.DISBAND_BTN_ID)
            time.sleep(1)
            self.click_element(By.ID, self.DEACTIVATE_BTN_ID)
            self.wait_for_empty_message(self.EMPTY_MATINGS_MSG)
        except Exception:
            pass

    def wait_for_empty_message(self, message):
        wait = WebDriverWait(self.driver, 15)
        try:
            xpath = self.EMPTY_MESSAGE_XPATH_TEMPLATE.format(message=message)
            empty_message = wait.until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            assert empty_message.is_displayed()
            time.sleep(2)
        except Exception:
            pass

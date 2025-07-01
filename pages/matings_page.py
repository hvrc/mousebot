import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MatingsPage(BasePage):
    MATINGS_TAB_XPATH = "//a[contains(@href, 'smdb/mating/list.do')]"
    WARNING_POPUP_XPATH = "//div[contains(@class, 'ui-dialog-buttonset')]/button/span[text()='OK']/.."
    HOME_BTN_XPATH = "//li[@id='home']//a[contains(@href, 'HomePage.do')]"
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"

    FIRST_MALE_CHECKBOX_CSS = "table#malemouseTable tbody input.cbox[type='checkbox']:first-of-type"
    FIRST_FEMALE_CHECKBOX_CSS = "table#femalemouseTable tbody input.cbox[type='checkbox']:first-of-type"
    ALL_FEMALE_CHECKBOXES_CSS = "table#femalemouseTable tbody input.cbox[type='checkbox']"

    NEW_MATINGS_BTN_ID = "newMatingMenuButton"
    SETUP_DATE_INPUT_ID = "setupDate"
    MATING_TAG_ID = "matingTag"
    STRAIN_SELECT_ID = "mouselineId"
    ADD_BTN_ID = "batchApply"
    MOVE_BREEDERS_BTN_ID = "submitBatchesAndMove"
    CREATE_UPDATE_CAGES_BTN_ID = "moveApply"
    DONE_BTN_ID = "backbtn"
    SELECT_ALL_MATINGS_ID = "cb_matinglist_table"
    DISBAND_BTN_ID = "disbandmatingButton"
    DEACTIVATE_BTN_ID = "applydisbandMating"
    EMPTY_MATINGS_MSG = "No matings to show!"

    NEW_LITTER_BTN_ID = "newLitter4MatingMenuButton"

    MATINGS_TAB = (By.XPATH, MATINGS_TAB_XPATH)
    NEW_MATINGS_BTN = (By.ID, NEW_MATINGS_BTN_ID)
    FIRST_MALE_CHECKBOX = (By.CSS_SELECTOR, FIRST_MALE_CHECKBOX_CSS)
    FIRST_FEMALE_CHECKBOX = (By.CSS_SELECTOR, FIRST_FEMALE_CHECKBOX_CSS)
    SETUP_DATE_INPUT = (By.ID, SETUP_DATE_INPUT_ID)
    MATING_TAG = (By.ID, MATING_TAG_ID)
    STRAIN_SELECT = (By.ID, STRAIN_SELECT_ID)
    ADD_BTN = (By.ID, ADD_BTN_ID)
    MOVE_BREEDERS_BTN = (By.ID, MOVE_BREEDERS_BTN_ID)
    CREATE_UPDATE_CAGES_BTN = (By.ID, CREATE_UPDATE_CAGES_BTN_ID)
    DONE_BTN = (By.ID, DONE_BTN_ID)
    WARNING_POPUP = (By.XPATH, WARNING_POPUP_XPATH)
    HOME_BTN = (By.XPATH, HOME_BTN_XPATH)
    ALL_FEMALE_CHECKBOXES = (By.CSS_SELECTOR, ALL_FEMALE_CHECKBOXES_CSS)
    NEW_LITTER_BTN = (By.ID, NEW_LITTER_BTN_ID)

    # click on new mating button
    def start_new_mating(self):
        self.click_element(*self.NEW_MATINGS_BTN)
        time.sleep(2)

    # in create a new mating page,
    # select first available male from records list
    def select_first_male(self):
        self.click_element(*self.FIRST_MALE_CHECKBOX)
        time.sleep(1)

    # in create a new mating page,
    # select first available female from records list
    def select_first_female(self):
        self.click_element(*self.FIRST_FEMALE_CHECKBOX)
        time.sleep(1)

    # in create a new mating page,
    # set the setup date for the mating
    def set_setup_date(self, date_str):
        date_input = self.find_element(*self.SETUP_DATE_INPUT)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_input)
        date_input.clear()
        date_input.send_keys(date_str)
        time.sleep(1)

    # in create a new mating page,
    # set the mating tag for the mating
    def set_mating_tag(self, tag):
        tag_input = self.find_element(*self.MATING_TAG)
        tag_input.clear()
        tag_input.send_keys(tag)
        time.sleep(1)

    # in create a new mating page,
    # select first available strain from the dropdown
    def select_first_strain(self):
        strain_select = self.find_element(*self.STRAIN_SELECT)
        select = Select(strain_select)
        for option in select.options:
            if option.get_attribute("value"):
                select.select_by_value(option.get_attribute("value"))
                break
    
    # in create a new mating page,
    # add the mating to the list
    def add_mating(self):
        self.click_element(*self.ADD_BTN)
        time.sleep(1)

    # in create a new mating page,
    # create a second mating record for a trio mating,
    # and add it
    def add_second_mating_if_available(self, tag):
        female_checkboxes = self.driver.find_elements(*self.ALL_FEMALE_CHECKBOXES)
        if len(female_checkboxes) > 1:
            female_checkboxes[1].click()
            self.set_mating_tag(tag)
            self.add_mating()

    # on create a new mating page,
    # create matings and move breeders into cages
    def move_breeders(self):
        self.click_element(*self.MOVE_BREEDERS_BTN)
        time.sleep(1)

    # this has been redundantly defined!
    # move animals page,
    # click on create/update cages button
    def create_update_cages(self):
        self.click_element(*self.CREATE_UPDATE_CAGES_BTN)
        time.sleep(1)

    # this has been redundantly defined!
    # move summary page,
    # click on done button
    def done(self):
        self.click_element(*self.DONE_BTN)
        time.sleep(1)

    # handle warning/error on create a new mating page
    def handle_warning_popup_and_go_home(self):
        self.click_element(*self.WARNING_POPUP)
        from pages.colony_page import ColonyPage
        ColonyPage(self.driver).go_home()

    # disband matings button in matings tab
    # then on disband mating page, click deactivate matings button,
    # do not move into new cages
    def disband_and_deactivate_all_matings(self):
        self.click_element(By.ID, self.SELECT_ALL_MATINGS_ID)
        time.sleep(1)
        self.click_element(By.ID, self.DISBAND_BTN_ID)
        time.sleep(1)
        self.click_element(By.ID, self.DEACTIVATE_BTN_ID)
        from pages.colony_page import ColonyPage
        ColonyPage(self.driver).wait_for_empty_message(self.EMPTY_MATINGS_MSG)

    def click_new_litter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEW_LITTER_BTN)
        ).click()
        time.sleep(1)

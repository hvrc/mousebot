import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .colony_page import ColonyPage

class LittersPage(BasePage):
    EMPTY_LITTERS_MSG = "No litters to show!"
    FIRST_MATING_CHECKBOX = (By.CSS_SELECTOR, "#matinglist_table tbody tr[id] input.cbox")
    DOB_INPUT = (By.ID, "birthDatePicker")
    CREATE_LITTERS_BTN = (By.ID, "editSaveNewLitter")
    POPUP_OK_BTN = (By.XPATH, "//div[contains(@class, 'ui-dialog-buttonset')]//span[text()='OK']/..")
    LITTERS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/litter/list.do')]")
    ADD_PUPS_BTN = (By.ID, "addPupsBtn")
    MALES_DROPDOWN = (By.ID, "males")
    SUBMIT_PUPS_BTN = (By.ID, "addPups")
    APPLY_BUTTON = (By.ID, "boxApply")
    WEAN_LITTERS_BTN = (By.ID, "weanLitterBtn")
    WEAN_MOVE_BTN = (By.ID, "editSubmitMove")
    CREATE_UPDATE_CAGES_BTN = (By.ID, "moveApply")
    DONE_BTN = (By.ID, "backbtn")
    TAG_PREFIX_INPUT = (By.ID, "tagPrefix")
    TAG_START_INDEX_INPUT = (By.ID, "tagStartIndex")
    SELECT_ALL_LITTERS = (By.ID, "cb_litter_table")
    DELETE_LITTERS_BTN = (By.ID, "deleteLitterBtn")
    LITTER_PUPS_CHECKBOX = (By.CSS_SELECTOR, "#litterTable tbody tr[id] input.cbox")
    PUP_WEAN_CHECKBOX = (By.CSS_SELECTOR, "#mouseTableWean tbody tr[id] input.cbox")
    EMPTY_MESSAGE = (By.XPATH, "//span[contains(text(), EMPTY_LITTERS_MSG)]")
    FIRST_LITTER_CHECKBOX = (By.XPATH, "//table[@id='litter_table']//tbody//tr[@id]//input[contains(@class, 'cbox')]")

    # select first mating checkbox, out of all mating records
    def select_first_mating(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_MATING_CHECKBOX)
        ).click()
        time.sleep(1)

    # in group edit mating,
    # enter date of birth
    # needs to be in MM-DD-YYYY format
    def enter_dob(self, dob):
        dob_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DOB_INPUT)
        )
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", dob_input)
        dob_input.clear()
        dob_input.send_keys(dob)
        time.sleep(1)

    # in group edit mating,
    # click create litters button
    def create_litters(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CREATE_LITTERS_BTN)
        ).click()
        time.sleep(1)

    # in group edit mating, success pop up after creating litters
    # in add pups page, success pop up after adding pups
    # works for delete case as well
    # after pressing ok you stay on the same page
    def confirm_popup(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(1)
        except Exception:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.POPUP_OK_BTN)
            ).click()
            time.sleep(1)

    # this helps us navigate to litters tab,
    # so that we can see the litter list
    def go_to_litters_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LITTERS_TAB)
        ).click()
        time.sleep(1)

    # selects the first litter checkbox,
    # from the list of litter records
    def select_first_litter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_LITTER_CHECKBOX)
        ).click()
        time.sleep(1)

    # click add pups button in litter page/tab
    def click_add_pups(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_PUPS_BTN)
        ).click()
        time.sleep(1)

    # in add pups page, 
    # select first litter pups checkbox
    def select_first_litter_pups(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LITTER_PUPS_CHECKBOX)
        ).click()
        time.sleep(1)

    # in add pups page,
    # select males dropdown
    def select_males_dropdown(self, value):
        males_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MALES_DROPDOWN)
        )
        Select(males_dropdown).select_by_value(value)
        time.sleep(1)

    # in add pups page,
    # click submit pups button
    def click_submit_pups(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_PUPS_BTN)
        ).click()
        time.sleep(1)

    # wean litter button in litter page/tab
    def click_wean_litters(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WEAN_LITTERS_BTN)
        ).click()
        time.sleep(1)

    # apply button on wean litter page
    # after adding details for weanlings
    def click_apply_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.APPLY_BUTTON)
        ).click()
        time.sleep(1)

    # on wean litter page,
    # select first weanling from records
    def select_first_pup_wean(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PUP_WEAN_CHECKBOX)
        ).click()
        time.sleep(1)

    # physical tag on wean litter page, two blanks
    def enter_physical_tag(self, prefix, start_index):
        tag_prefix = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TAG_PREFIX_INPUT)
        )
        tag_prefix.clear()
        tag_prefix.send_keys(prefix)
        tag_start = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TAG_START_INDEX_INPUT)
        )
        tag_start.clear()
        tag_start.send_keys(str(start_index))
        time.sleep(1)

    # button on wean litter page
    def click_create_update_cages_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CREATE_UPDATE_CAGES_BTN)
        ).click()
        time.sleep(1)

    # this has been redundantly defined!
    # move animals
    def click_wean_move_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WEAN_MOVE_BTN)
        ).click()
        time.sleep(1)

    # this has been redundantly defined!
    # move summary
    def click_done_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DONE_BTN)
        ).click()
        time.sleep(1)

    # trash can button, handle popup
    def delete_all_litters(self):
        select_all = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SELECT_ALL_LITTERS)
        )
        select_all.click()
        time.sleep(1)
        delete_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELETE_LITTERS_BTN)
        )
        delete_btn.click()
        self.confirm_popup()
        colonyPage = ColonyPage(self.driver)
        colonyPage.wait_for_empty_message(self.EMPTY_LITTERS_MSG)
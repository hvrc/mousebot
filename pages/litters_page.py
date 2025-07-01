import time
from .base_page import BasePage
from .colony_page import ColonyPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LittersPage(BasePage):
    POPUP_OK_BTN_XPATH = "//div[contains(@class, 'ui-dialog-buttonset')]//span[text()='OK']/.."
    HOME_BUTTON_XPATH = "//li[@id='home']//a[contains(@href, 'HomePage.do')]"
    LITTERS_TAB_XPATH = "//a[contains(@href, 'smdb/litter/list.do')]"
    FIRST_LITTER_CHECKBOX_XPATH = "//table[@id='litter_table']//tbody//tr[@id]//input[contains(@class, 'cbox')]"
    # ANIMALS_TAB_XPATH = "//a[contains(@href, 'smdb/mouse/list.do') and contains(text(), 'Animals')]"
    EMPTY_MESSAGE_XPATH = "//span[contains(text(), 'No litters to show!')]"
    LITTER_PUPS_CHECKBOX_CSS = "#litterTable tbody tr[id] input.cbox"
    PUP_WEAN_CHECKBOX_CSS = "#mouseTableWean tbody tr[id] input.cbox"

    FIRST_MATING_CHECKBOX_ID = "matinglist_table"
    NEW_LITTER_BTN_ID = "newLitter4MatingMenuButton"
    DOB_INPUT_ID = "birthDatePicker"
    CREATE_LITTERS_BTN_ID = "editSaveNewLitter"
    ADD_PUPS_BTN_ID = "addPupsBtn"
    MALES_DROPDOWN_ID = "males"
    SUBMIT_PUPS_BTN_ID = "addPups"
    APPLY_BUTTON_ID = "boxApply"
    WEAN_LITTERS_BTN_ID = "weanLitterBtn"
    WEAN_MOVE_BTN_ID = "editSubmitMove"
    CREATE_UPDATE_CAGES_BTN_ID = "moveApply"
    DONE_BTN_ID = "backbtn"
    TAG_PREFIX_INPUT_ID = "tagPrefix"
    TAG_START_INDEX_INPUT_ID = "tagStartIndex"
    SELECT_ALL_LITTERS_ID = "cb_litter_table"
    DELETE_LITTERS_BTN_ID = "deleteLitterBtn"
    EMPTY_LITTERS_MSG = "No litters to show!"

    FIRST_MATING_CHECKBOX = (By.CSS_SELECTOR, "#matinglist_table tbody tr[id] input.cbox")
    NEW_LITTER_BTN = (By.ID, NEW_LITTER_BTN_ID)
    DOB_INPUT = (By.ID, DOB_INPUT_ID)
    CREATE_LITTERS_BTN = (By.ID, CREATE_LITTERS_BTN_ID)
    POPUP_OK_BTN = (By.XPATH, POPUP_OK_BTN_XPATH)
    HOME_BUTTON = (By.XPATH, HOME_BUTTON_XPATH)
    LITTERS_TAB = (By.XPATH, LITTERS_TAB_XPATH)
    ADD_PUPS_BTN = (By.ID, ADD_PUPS_BTN_ID)
    MALES_DROPDOWN = (By.ID, MALES_DROPDOWN_ID)
    SUBMIT_PUPS_BTN = (By.ID, SUBMIT_PUPS_BTN_ID)
    APPLY_BUTTON = (By.ID, APPLY_BUTTON_ID)
    WEAN_LITTERS_BTN = (By.ID, WEAN_LITTERS_BTN_ID)
    WEAN_MOVE_BTN = (By.ID, WEAN_MOVE_BTN_ID)
    CREATE_UPDATE_CAGES_BTN = (By.ID, CREATE_UPDATE_CAGES_BTN_ID)
    DONE_BTN = (By.ID, DONE_BTN_ID)
    TAG_PREFIX_INPUT = (By.ID, TAG_PREFIX_INPUT_ID)
    TAG_START_INDEX_INPUT = (By.ID, TAG_START_INDEX_INPUT_ID)
    SELECT_ALL_LITTERS = (By.ID, SELECT_ALL_LITTERS_ID)
    DELETE_LITTERS_BTN = (By.ID, DELETE_LITTERS_BTN_ID)
    LITTER_PUPS_CHECKBOX = (By.CSS_SELECTOR, LITTER_PUPS_CHECKBOX_CSS)
    PUP_WEAN_CHECKBOX = (By.CSS_SELECTOR, PUP_WEAN_CHECKBOX_CSS)
    # ANIMALS_TAB = (By.XPATH, ANIMALS_TAB_XPATH)
    EMPTY_MESSAGE = (By.XPATH, EMPTY_MESSAGE_XPATH)
    FIRST_LITTER_CHECKBOX = (By.XPATH, FIRST_LITTER_CHECKBOX_XPATH)

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
        from selenium.webdriver.support.ui import Select
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
        ColonyPage(self.driver).wait_for_empty_message(self.EMPTY_LITTERS_MSG)
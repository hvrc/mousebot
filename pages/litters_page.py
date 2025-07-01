from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LittersPage(BasePage):
    # XPATH selectors
    POPUP_OK_BTN_XPATH = "//div[contains(@class, 'ui-dialog-buttonset')]//span[text()='OK']/.."
    HOME_BUTTON_XPATH = "//li[@id='home']//a[contains(@href, 'HomePage.do')]"
    LITTERS_TAB_XPATH = "//a[contains(@href, 'smdb/litter/list.do')]"
    FIRST_LITTER_CHECKBOX_XPATH = "//table[@id='litter_table']//tbody//tr[@id]//input[contains(@class, 'cbox')]"
    ANIMALS_TAB_XPATH = "//a[contains(@href, 'smdb/mouse/list.do') and contains(text(), 'Animals')]"
    EMPTY_MESSAGE_XPATH = "//span[contains(text(), 'No litters to show!')]"
    
    # ID selectors
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

    # Tuple selectors
    FIRST_MATING_CHECKBOX = (By.CSS_SELECTOR, "#matinglist_table tbody tr[id] input.cbox")
    NEW_LITTER_BTN = (By.ID, NEW_LITTER_BTN_ID)
    DOB_INPUT = (By.ID, DOB_INPUT_ID)
    CREATE_LITTERS_BTN = (By.ID, CREATE_LITTERS_BTN_ID)
    POPUP_OK_BTN = (By.XPATH, POPUP_OK_BTN_XPATH)
    HOME_BUTTON = (By.XPATH, HOME_BUTTON_XPATH)
    LITTERS_TAB = (By.XPATH, LITTERS_TAB_XPATH)

    def select_first_mating(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_MATING_CHECKBOX)
        ).click()
        time.sleep(0.5)

    def click_new_litter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEW_LITTER_BTN)
        ).click()
        time.sleep(1)

    def enter_dob(self, dob):
        dob_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DOB_INPUT)
        )
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", dob_input)
        dob_input.clear()
        dob_input.send_keys(dob)
        time.sleep(0.5)

    def create_litters(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CREATE_LITTERS_BTN)
        ).click()
        time.sleep(0.5)

    def confirm_popup(self):
        try:
            # Try JavaScript alert first
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(0.5)
        except Exception:
            # Fallback to UI-based dialog
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.POPUP_OK_BTN)
            ).click()
            time.sleep(0.5)

    def go_to_litters_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LITTERS_TAB)
        ).click()
        time.sleep(1)

    def select_first_litter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_LITTER_CHECKBOX_XPATH))
        ).click()
        time.sleep(0.5)

    def click_add_pups(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.ADD_PUPS_BTN_ID))
        ).click()
        time.sleep(0.5)

    def select_first_litter_pups(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#litterTable tbody tr[id] input.cbox"))
        ).click()
        time.sleep(0.5)

    def select_males_dropdown(self, value):
        from selenium.webdriver.support.ui import Select
        males_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.MALES_DROPDOWN_ID))
        )
        Select(males_dropdown).select_by_value(value)
        time.sleep(0.5)

    def click_submit_pups(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.SUBMIT_PUPS_BTN_ID))
        ).click()
        time.sleep(0.5)

    def click_apply_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.APPLY_BUTTON_ID))
        ).click()
        time.sleep(1)

    def click_wean_litters(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.WEAN_LITTERS_BTN_ID))
        ).click()
        time.sleep(1)

    def select_first_pup_wean(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mouseTableWean tbody tr[id] input.cbox"))
        ).click()
        time.sleep(0.5)

    def enter_physical_tag(self, prefix, start_index):
        tag_prefix = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TAG_PREFIX_INPUT_ID))
        )
        tag_prefix.clear()
        tag_prefix.send_keys(prefix)
        tag_start = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TAG_START_INDEX_INPUT_ID))
        )
        tag_start.clear()
        tag_start.send_keys(str(start_index))
        time.sleep(0.5)

    def click_wean_move_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.WEAN_MOVE_BTN_ID))
        ).click()
        time.sleep(1)

    def click_create_update_cages_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.CREATE_UPDATE_CAGES_BTN_ID))
        ).click()
        time.sleep(1)

    def click_done_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.DONE_BTN_ID))
        ).click()
        time.sleep(1)

    def go_to_animals_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ANIMALS_TAB_XPATH))
        ).click()
        time.sleep(1)

    def go_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HOME_BUTTON)
        ).click()
        time.sleep(1)

    def delete_all_litters(self):
        select_all = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.SELECT_ALL_LITTERS_ID))
        )
        if select_all.is_displayed() and select_all.is_enabled():
            select_all.click()
            time.sleep(0.5)
            delete_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.DELETE_LITTERS_BTN_ID))
            )
            delete_btn.click()
            self.confirm_popup()
            self.wait_for_empty_message()
        else:
            print("No litters to delete or select-all checkbox not interactable.")

    def wait_for_empty_message(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMPTY_MESSAGE_XPATH))
        )
        time.sleep(1)
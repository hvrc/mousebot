from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LittersPage(BasePage):
    # XPATH selectors as class variables
    POPUP_OK_BTN_XPATH = "//div[contains(@class, 'ui-dialog-buttonset')]/button/span[text()='OK']/.."
    HOME_BUTTON_XPATH = "//li[@id='home']//a[contains(@href, 'HomePage.do')]"
    LITTERS_TAB_XPATH = "//a[contains(@href, 'smdb/litter/list.do')]"
    FIRST_LITTER_CHECKBOX_XPATH = "//table[@id='litter_table']//tbody//tr[@id]//input[contains(@class, 'cbox')]"
    ANIMALS_TAB_XPATH = "//a[contains(@href, 'smdb/mouse/list.do') and contains(text(), 'Animals')]"
    # ID selectors as class variables
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

    FIRST_MATING_CHECKBOX = (By.CSS_SELECTOR, "#matinglist_table tbody tr[id] input.cbox")
    NEW_LITTER_BTN = (By.ID, NEW_LITTER_BTN_ID)
    DOB_INPUT = (By.ID, DOB_INPUT_ID)
    CREATE_LITTERS_BTN = (By.ID, CREATE_LITTERS_BTN_ID)
    POPUP_OK_BTN = (By.XPATH, POPUP_OK_BTN_XPATH)
    HOME_BUTTON = (By.XPATH, HOME_BUTTON_XPATH)
    LITTERS_TAB = (By.XPATH, LITTERS_TAB_XPATH)

    def select_first_mating(self):
        self.click_element(*self.FIRST_MATING_CHECKBOX)
        time.sleep(1)

    def click_new_litter(self):
        self.click_element(By.ID, self.NEW_LITTER_BTN_ID)
        time.sleep(2)

    def enter_dob(self, dob):
        dob_input = self.find_element(By.ID, self.DOB_INPUT_ID)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", dob_input)
        dob_input.clear()
        dob_input.send_keys(dob)
        time.sleep(1)

    def create_litters(self):
        self.click_element(By.ID, self.CREATE_LITTERS_BTN_ID)
        time.sleep(1)

    def confirm_popup(self):
        self.click_element(By.XPATH, self.POPUP_OK_BTN_XPATH)
        time.sleep(1)

    def go_to_litters_tab(self):
        self.click_element(By.XPATH, self.LITTERS_TAB_XPATH)
        time.sleep(2)

    def select_first_litter(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_LITTER_CHECKBOX_XPATH))
        )
        checkbox.click()
        time.sleep(1)

    def click_add_pups(self):
        self.click_element(By.ID, self.ADD_PUPS_BTN_ID)
        time.sleep(1)

    def select_first_litter_pups(self):
        self.click_element(By.CSS_SELECTOR, "#litterTable tbody tr[id] input.cbox")
        time.sleep(1)

    def select_males_dropdown(self, value):
        from selenium.webdriver.support.ui import Select
        males_dropdown = self.find_element(By.ID, self.MALES_DROPDOWN_ID)
        select = Select(males_dropdown)
        select.select_by_value(value)
        time.sleep(1)

    def click_submit_pups(self):
        self.click_element(By.ID, self.SUBMIT_PUPS_BTN_ID)
        time.sleep(1)

    def click_apply_button(self):
        self.click_element(By.ID, self.APPLY_BUTTON_ID)
        time.sleep(2)

    def click_wean_litters(self):
        self.click_element(By.ID, self.WEAN_LITTERS_BTN_ID)
        time.sleep(2)

    def select_first_pup_wean(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mouseTableWean tbody tr[id] input.cbox"))
        )
        checkbox.click()
        time.sleep(1)

    def enter_physical_tag(self, prefix, start_index):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        tag_prefix = wait.until(EC.presence_of_element_located((By.ID, self.TAG_PREFIX_INPUT_ID)))
        tag_prefix.clear()
        tag_prefix.send_keys(prefix)
        tag_start = wait.until(EC.presence_of_element_located((By.ID, self.TAG_START_INDEX_INPUT_ID)))
        tag_start.clear()
        tag_start.send_keys(str(start_index))
        time.sleep(1)

    def click_wean_move_button(self):
        self.click_element(By.ID, self.WEAN_MOVE_BTN_ID)
        time.sleep(2)

    def click_create_update_cages_button(self):
        self.click_element(By.ID, self.CREATE_UPDATE_CAGES_BTN_ID)
        time.sleep(2)

    def click_done_button(self):
        self.click_element(By.ID, self.DONE_BTN_ID)
        time.sleep(2)

    def go_to_animals_tab(self):
        self.click_element(By.XPATH, self.ANIMALS_TAB_XPATH)
        time.sleep(2)

    def go_home(self):
        self.click_element(By.XPATH, self.HOME_BUTTON_XPATH)
        time.sleep(2)

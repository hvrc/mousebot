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

    def go_to_litters_tab(self):
        self.click_element(*self.LITTERS_TAB)
        time.sleep(2)

    def select_first_litter(self):
        # Select the first available litter checkbox in the jqGrid table
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#litter_table tbody tr[id] input.cbox"))
        )
        checkbox.click()
        import time; time.sleep(1)

    def click_add_pups(self):
        self.click_element(By.ID, "addPupsBtn")
        time.sleep(1)

    def select_first_litter_pups(self):
        self.click_element(By.CSS_SELECTOR, "#litterTable tbody tr[id] input.cbox")
        time.sleep(1)

    def select_males_dropdown(self, value):
        from selenium.webdriver.support.ui import Select
        males_dropdown = self.find_element(By.ID, "males")
        select = Select(males_dropdown)
        select.select_by_value(value)
        time.sleep(1)

    def click_submit_pups(self):
        self.click_element(By.ID, "addPups")
        time.sleep(1)

    def click_apply_button(self):
        self.click_element(By.ID, "boxApply")
        import time; time.sleep(2)

    def click_wean_litters(self):
        self.click_element(By.ID, "weanLitterBtn")
        import time; time.sleep(2)

    def select_first_pup_wean(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        checkbox = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mouseTableWean tbody tr[id] input.cbox"))
        )
        checkbox.click()
        import time; time.sleep(1)

    def enter_physical_tag(self, prefix, start_index):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        tag_prefix = wait.until(EC.presence_of_element_located((By.ID, "tagPrefix")))
        tag_prefix.clear()
        tag_prefix.send_keys(prefix)
        tag_start = wait.until(EC.presence_of_element_located((By.ID, "tagStartIndex")))
        tag_start.clear()
        tag_start.send_keys(str(start_index))
        import time; time.sleep(1)

    def click_wean_move_button(self):
        self.click_element(By.ID, "editSubmitMove")
        import time; time.sleep(2)

    def click_create_update_cages_button(self):
        self.click_element(By.ID, "moveApply")
        import time; time.sleep(2)

    def click_done_button(self):
        self.click_element(By.ID, "backbtn")
        import time; time.sleep(2)

    def go_to_animals_tab(self):
        self.click_element(By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do') and contains(text(), 'Animals')]")
        import time; time.sleep(2)

    def go_home(self):
        self.click_element(*self.HOME_BUTTON)
        import time; time.sleep(2)

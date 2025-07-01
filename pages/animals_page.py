import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AnimalsPage(BasePage):

    # id selectors, xpath selectors, and messages
    ANIMALS_TAB_ID = "mice"
    SELECT_ALL_ANIMALS_ID = "cb_mouseTable"
    DELETE_ANIMALS_BTN_ID = "deleteMouseMenuButton"
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"
    EMPTY_ANIMALS_MSG = "No animals to show!"

    # from colony mmodule, click blue animals tab
    def go_to_animals_tab(self):
        self.click_element(By.ID, self.ANIMALS_TAB_ID)
        time.sleep(1)

    # try to delete all animals up to 5 times,
    # correct implementation is to read how many pages of records exist,
    # and run deletion for each page
    def delete_all_animals(self):
        max_attempts = 5
        for _ in range(max_attempts):
            try:
                self.click_element(By.ID, self.SELECT_ALL_ANIMALS_ID)
                time.sleep(1)
                self.click_element(By.ID, self.DELETE_ANIMALS_BTN_ID)
                self.handle_confirm_dialog()
                self.wait_for_empty_message(self.EMPTY_ANIMALS_MSG)
                return
            except Exception:
                pass
    
    # chrome confirm dialog box
    def handle_confirm_dialog(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        confirm = self.driver.switch_to.alert
        confirm.accept()
        time.sleep(1)
    
    # this shuold be in colony page!
    # the message should be defined here
    # confirm that all animals ahve been deleted
    def wait_for_empty_message(self, message):
        wait = WebDriverWait(self.driver, 10)
        xpath = self.EMPTY_MESSAGE_XPATH_TEMPLATE.format(message=message)
        empty_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        assert empty_message.is_displayed()
        time.sleep(1)
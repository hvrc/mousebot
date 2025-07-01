from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AnimalsPage(BasePage):
    ANIMALS_TAB_ID = "mice"
    SELECT_ALL_ANIMALS_ID = "cb_mouseTable"
    DELETE_ANIMALS_BTN_ID = "deleteMouseMenuButton"
    EMPTY_ANIMALS_MSG = "No animals to show!"
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"

    def go_to_animals_tab(self):
        self.click_element(By.ID, self.ANIMALS_TAB_ID)
        time.sleep(2)

    def delete_all_animals(self):
        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                self.click_element(By.ID, self.SELECT_ALL_ANIMALS_ID)
                time.sleep(1)
                self.click_element(By.ID, self.DELETE_ANIMALS_BTN_ID)
                self.handle_confirm_dialog()
                self.wait_for_empty_message(self.EMPTY_ANIMALS_MSG)
                return
            except Exception:
                pass

    def handle_confirm_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            confirm = self.driver.switch_to.alert
            confirm.accept()
            time.sleep(3)
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

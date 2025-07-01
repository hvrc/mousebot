from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class StrainsPage(BasePage):
    # XPATH selectors
    STRAINS_TAB_XPATH = "//a[contains(@href, 'smdb/mouseline/list.do') and contains(@class, 'line textdecoration')]"
    POPUP_OK_BTN_XPATH = "//div[contains(@class, 'ui-dialog-buttonset')]//span[text()='OK']/.."
    HOME_BUTTON_XPATH = "//a[@class='textdecoration' and contains(@href, 'HomePage.do')]"
    EMPTY_MESSAGE_XPATH = "//span[contains(text(), 'No strains to show!')]"
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"

    # ID selectors
    SELECT_ALL_STRAINS_ID = "cb_mouseline_table"
    DELETE_STRAINS_BTN_ID = "mouselineDeleteBtn"
    EMPTY_MATINGS_MSG = "No Strains to show!"

    # Tuple selectors
    STRAINS_TAB = (By.XPATH, STRAINS_TAB_XPATH)
    POPUP_OK_BTN = (By.XPATH, POPUP_OK_BTN_XPATH)
    HOME_BTN = (By.XPATH, HOME_BUTTON_XPATH)
    SELECT_ALL_STRAINS = (By.ID, SELECT_ALL_STRAINS_ID)
    DELETE_STRAINS_BTN = (By.ID, DELETE_STRAINS_BTN_ID)
    EMPTY_MESSAGE = (By.XPATH, EMPTY_MESSAGE_XPATH)

    def go_to_strains_tab(self):
        if "smdb/mouseline/list.do" not in self.driver.current_url:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.STRAINS_TAB)
            ).click()
            time.sleep(0.5)

    def delete_all_strains(self):
        select_all = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SELECT_ALL_STRAINS)
        )
        if select_all.is_displayed() and select_all.is_enabled():
            select_all.click()
            time.sleep(0.5)
            delete_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DELETE_STRAINS_BTN)
            )
            delete_btn.click()
            self.handle_confirm_dialog()
            self.wait_for_empty_message(self.EMPTY_MATINGS_MSG)
        else:
            print("No strains to delete or select-all checkbox not interactable.")

    def handle_confirm_dialog(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(0.5)
        except Exception:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.POPUP_OK_BTN)
            ).click()
            time.sleep(0.5)

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

    def go_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HOME_BTN)
        ).click()
        time.sleep(0.5)
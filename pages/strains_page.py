import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .colony_page import ColonyPage

class StrainsPage(BasePage):
    STRAINS_TAB = (By.XPATH, "//a[contains(@href, 'smdb/mouseline/list.do') and contains(@class, 'line textdecoration')]")
    POPUP_OK_BTN = (By.XPATH, "//div[contains(@class, 'ui-dialog-buttonset')]//span[text()='OK']/..")
    HOME_BTN = (By.XPATH, "//a[@class='textdecoration' and contains(@href, 'HomePage.do')]")
    EMPTY_MESSAGE = (By.XPATH, "//span[contains(text(), 'No strains to show!')]")
    EMPTY_MESSAGE_XPATH_TEMPLATE = "//span[contains(text(), '{message}')]"
    SELECT_ALL_STRAINS = (By.ID, "cb_mouseline_table")
    DELETE_STRAINS_BTN = (By.ID, "mouselineDeleteBtn")
    EMPTY_MATINGS_MSG = "No Strains to show!"

    # select checkbox for all strains,
    # and delete them via trash can button
    def delete_all_strains(self):
        select_all = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SELECT_ALL_STRAINS)
        )
        if select_all.is_displayed() and select_all.is_enabled():
            select_all.click()
            time.sleep(1)
            delete_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DELETE_STRAINS_BTN)
            )
            delete_btn.click()
            self.handle_confirm_dialog()
            colonyPage = ColonyPage(self.driver)
            colonyPage.wait_for_empty_message(self.EMPTY_MATINGS_MSG)
        else:
            print("No strains to delete or select-all checkbox not interactable.")
import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.colony_page import ColonyPage

class AnimalsPage(BasePage):

    # id selectors, xpath selectors, and messages
    ANIMALS_TAB_ID = "mice"
    SELECT_ALL_ANIMALS_ID = "cb_mouseTable"
    DELETE_ANIMALS_BTN_ID = "deleteMouseMenuButton"
    EMPTY_ANIMALS_MSG = "No animals to show!"

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
                colony_page = ColonyPage(self.driver)
                colony_page.wait_for_empty_message(self.EMPTY_ANIMALS_MSG)
                return
            except Exception:
                pass
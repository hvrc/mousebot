from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "inputUsernameEmail")
    PASSWORD_FIELD = (By.ID, "inputPassword")
    LOGIN_BUTTON = (By.ID, "secureLogin")
    MODULES_BUTTON = (By.ID, "apps-selected-open")
    COLONY_BUTTON = (By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]")

    def login(self, username, password):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.click_element(*self.LOGIN_BUTTON)

    def navigate_to_colony(self):
        self.click_element(*self.MODULES_BUTTON)
        self.click_element(*self.COLONY_BUTTON)
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "inputUsernameEmail")
    PASSWORD_FIELD = (By.ID, "inputPassword")
    LOGIN_BUTTON = (By.ID, "secureLogin")
    MODULES_BUTTON = (By.ID, "apps-selected-open")
    COLONY_BUTTON = (By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]")

    def login(self, username, password):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.click_element(*self.LOGIN_BUTTON)

    # this should be in home page!
    def navigate_to_colony(self):
        self.click_element(*self.MODULES_BUTTON)
        self.click_element(*self.COLONY_BUTTON)

    # where is this used?
    def go_to_login_page(self, url):
        self.driver.get(url)

    # confirm login by checking if on home page
    def is_on_home_page(self):
        time.sleep(1)
        return "homepage.do" in self.driver.current_url.lower()
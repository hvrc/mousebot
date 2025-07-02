import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "inputUsernameEmail")
    PASSWORD_FIELD = (By.ID, "inputPassword")
    LOGIN_BUTTON = (By.ID, "secureLogin")

    def login(self, username, password):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.click_element(*self.LOGIN_BUTTON)

    # 
    def go_to_login_page(self, url):
        self.driver.get(url)

    # confirm login by checking if on home page
    def is_on_home_page(self):
        time.sleep(1)
        return "homepage.do" in self.driver.current_url.lower()
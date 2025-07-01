from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# wait for elements to be present or clickable
# finds elements and clicks them
class BasePage:
    CONFIRM_OK_BTN_XPATH = "//div[contains(@class, 'ui-dialog-buttonset')]//span[text()='OK']/.."

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def handle_confirm_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(1)
        except Exception:
            # fallback for custom popups
            try:
                ok_btn = self.wait.until(EC.element_to_be_clickable((
                    By.XPATH, self.CONFIRM_OK_BTN_XPATH
                )))
                ok_btn.click()
                time.sleep(1)
            except Exception:
                pass
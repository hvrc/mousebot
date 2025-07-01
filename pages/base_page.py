from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# wait for elements to be present or clickable
# finds elements and clicks them
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
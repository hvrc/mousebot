import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time

def test_login(driver, config):
    login_page = LoginPage(driver)
    
    # Navigate to login page
    driver.get(config['url'])
    
    # Login
    login_page.login(config['username'], config['password'])
    
    # Wait for home button and click it
    wait = WebDriverWait(driver, 10)
    home_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]"))
    )
    home_button.click()
    
    # Wait for navigation and verify we're on home page
    time.sleep(2)
    assert "homepage.do" in driver.current_url.lower()
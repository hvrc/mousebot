import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time

def test_reset_litters(driver, config):
    # Initialize page objects
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, 10)
    
    # Navigate to colony module
    login_page.navigate_to_colony()
    
    # Wait for and click on Litters tab
    litters_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/litter/list.do')]"))
    )
    litters_tab.click()
    
    # Wait for the litters table to load and select all records
    select_all_checkbox = wait.until(
        EC.element_to_be_clickable((By.ID, "cb_litter_table"))
    )
    select_all_checkbox.click()
    
    # Navigate back to home
    home_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]"))
    )
    home_button.click()
    
    # Verify we're on home page
    time.sleep(2)
    assert "homepage.do" in driver.current_url.lower()

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_mating_invalid_date(driver, config):
    wait = WebDriverWait(driver, 10)

    # Go to Colony module
    modules_icon = wait.until(
        EC.element_to_be_clickable((By.ID, "apps-selected-open"))
    )
    modules_icon.click()
    colony_module = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]"))
    )
    colony_module.click()
    time.sleep(2)

    # Go to Matings tab
    matings_tab = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/mating/list.do')]"))
    )
    matings_tab.click()
    time.sleep(2)

    # Click New Matings button
    new_matings_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "newMatingMenuButton"))
    )
    new_matings_btn.click()
    time.sleep(2)

    # Select first available male
    first_male_checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "table#malemouseTable tbody input.cbox[type='checkbox']:first-of-type"))
    )
    first_male_checkbox.click()
    time.sleep(1)

    # Select first available female
    first_female_checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "table#femalemouseTable tbody input.cbox[type='checkbox']:first-of-type"))
    )
    first_female_checkbox.click()
    time.sleep(1)

    # Set up date earlier than wean date (e.g., Jan 2 2025)
    date_input = wait.until(
        EC.presence_of_element_located((By.ID, "setupDate"))
    )
    driver.execute_script("arguments[0].removeAttribute('readonly')", date_input)
    date_input.clear()
    date_input.send_keys("2025-01-02")
    time.sleep(1)
    driver.execute_script("arguments[0].value = arguments[1]", date_input, "01-02-2025")
    time.sleep(1)

    # Click Add button
    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "batchApply"))
    )
    add_button.click()
    time.sleep(1)

    # Verify pop-up with warning message appears and click OK
    popup_ok_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ui-dialog-buttonset')]/button/span[text()='OK']/.."))
    )
    popup_ok_btn.click()
    time.sleep(1)

    # Navigate back to home page
    home_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]"))
    )
    home_button.click()
    time.sleep(2)
    assert "homepage.do" in driver.current_url.lower()

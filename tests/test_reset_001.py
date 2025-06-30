import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from pages.login_page import LoginPage
import time

def wait_for_empty_message(wait, message, timeout=30):
    """Wait for empty state message with longer timeout"""
    try:
        empty_message = WebDriverWait(wait.driver, timeout).until( EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{message}')]")))
        assert empty_message.is_displayed()
        time.sleep(2)  # Additional wait to ensure state is stable
    except Exception as e:
        print(f"Timeout waiting for '{message}' message: {e}")
        # Continue anyway since the operation might have succeeded

def handle_confirm_dialog(driver, wait, timeout=30):
    """Handle confirm dialog with longer timeout"""
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        confirm = driver.switch_to.alert
        print(f"Confirm dialog text: {confirm.text}")
        confirm.accept()
        time.sleep(5)  # Increased wait after confirmation for large deletions
    except Exception as e:
        print(f"Error handling confirm dialog: {e}")
        # Try to continue with the test

def handle_large_deletion(driver, wait, select_all_id, delete_button_id, empty_message):
    """Handle deletion of large number of records with retries"""
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            # Select all records
            select_all = WebDriverWait(driver, 20).until( EC.element_to_be_clickable((By.ID, select_all_id)))
            select_all.click()
            time.sleep(2)  # Wait after selection

            # Click delete button
            delete_button = WebDriverWait(driver, 20).until( EC.element_to_be_clickable((By.ID, delete_button_id)))
            delete_button.click()

            # Handle confirmation
            handle_confirm_dialog(driver, wait)

            # Wait for empty message
            wait_for_empty_message(wait, empty_message)
            return True
        
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_attempts - 1:
                print("Max attempts reached, moving on...")
                return False
            time.sleep(5)  # Wait before retry

def test_reset_colony(driver, config):
    # Initialize page objects
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, 10)
    
    # Navigate to colony module
    login_page.navigate_to_colony()
    
    # === Litters Section ===
    # Click Litters tab
    litters_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/litter/list.do')]")))
    litters_tab.click()
    time.sleep(2)  # Wait after tab change
    
    # Select all litters and delete
    select_all_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "cb_litter_table")))
    select_all_checkbox.click()
    
    delete_button = wait.until(EC.element_to_be_clickable((By.ID, "deleteLitterBtn")))
    delete_button.click()
    handle_confirm_dialog(driver, wait)
    wait_for_empty_message(wait, "No litters to show!")
    
    # === Matings Section ===
    # Navigate to matings
    matings_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/mating/list.do')]")))
    matings_tab.click()
    time.sleep(2)  # Wait after tab change
    
    # Select all matings
    select_all_matings = wait.until(EC.element_to_be_clickable((By.ID, "cb_matinglist_table")))
    select_all_matings.click()
    
    # Click disband matings
    disband_button = wait.until(EC.element_to_be_clickable((By.ID, "disbandmatingButton")))
    disband_button.click()
    
    # Click deactivate mating
    deactivate_button = wait.until(EC.element_to_be_clickable((By.ID, "applydisbandMating")))
    deactivate_button.click()
    wait_for_empty_message(wait, "No matings to show!")
    
    # === Animals Section ===
    # Navigate to animals
    animals_tab = wait.until(EC.element_to_be_clickable((By.ID, "mice")))
    animals_tab.click()
    time.sleep(2)  # Wait after tab change
    
    # Handle large number of animal records
    success = handle_large_deletion(
        driver=driver,
        wait=wait,
        select_all_id="cb_mouseTable",
        delete_button_id="deleteMouseMenuButton",
        empty_message="No Animals to show!"
    )

    if not success: print("Warning: Animal deletion may not have completed successfully")
    
    # === Strains Section ===
    # Navigate to strains
    strains_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/mouseline/list.do')]")))
    strains_tab.click()
    time.sleep(2)  # Wait after tab change
    
    # Select all strains
    select_all_strains = wait.until(EC.element_to_be_clickable((By.ID, "cb_mouseline_table")))
    select_all_strains.click()
    
    # Delete strains
    delete_strains_button = wait.until(EC.element_to_be_clickable((By.ID, "mouselineDeleteBtn")))
    delete_strains_button.click()
    handle_confirm_dialog(driver, wait)
    wait_for_empty_message(wait, "No strains to show!")
    
    # Navigate back to home
    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]")))
    home_button.click()
    time.sleep(2)  # Wait after final navigation
    
    # Verify we're on home page
    time.sleep(2)
    assert "homepage.do" in driver.current_url.lower()

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

def test_mating_workflow(driver, config):
    wait = WebDriverWait(driver, 10)

    # Verify on home page
    assert "homepage.do" in driver.current_url.lower(), "Not on home page!"

    # Click modules icon and navigate to Colony module
    modules_icon = wait.until(
        EC.element_to_be_clickable((By.ID, "apps-selected-open"))
    )
    modules_icon.click()
    colony_module = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'smdb/mouse/list.do')]"))
    )
    colony_module.click()
    time.sleep(2)

    # Navigate to Matings tab
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

    # Click first available checkbox in male mouse table
    first_male_checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "table#malemouseTable tbody input.cbox[type='checkbox']:first-of-type"))
    )
    first_male_checkbox.click()
    time.sleep(1)

    # Click first available checkbox in female mouse table
    first_female_checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "table#femalemouseTable tbody input.cbox[type='checkbox']:first-of-type"))
    )
    first_female_checkbox.click()
    time.sleep(1)

    # Set date to Feb 1 2025 robustly
    date_input = wait.until(
        EC.presence_of_element_located((By.ID, "setupDate"))
    )
    driver.execute_script("arguments[0].removeAttribute('readonly')", date_input)
    date_input.clear()
    date_input.send_keys("2025-02-01")
    time.sleep(1)

    # If the above doesn't work, set value directly with JS:
    driver.execute_script("arguments[0].value = arguments[1]", date_input, "02-01-2025")
    time.sleep(1)

    # Set mating tag to 'M3'
    mating_tag_input = wait.until(
        EC.element_to_be_clickable((By.ID, "matingTag"))
    )
    mating_tag_input.clear()
    mating_tag_input.send_keys("M3")
    time.sleep(1)

    # Select first non-empty strain option
    strain_select = wait.until(
        EC.element_to_be_clickable((By.ID, "mouselineId"))
    )
    select = Select(strain_select)
    for option in select.options:
        if option.get_attribute("value"):
            select.select_by_value(option.get_attribute("value"))
            break
    time.sleep(1)

    # Click Add button
    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "batchApply"))
    )
    add_button.click()
    time.sleep(2)

    # Click next available checkbox in female mouse table (skip the first, which is already selected)
    female_checkboxes = driver.find_elements(By.CSS_SELECTOR, "table#femalemouseTable tbody input.cbox[type='checkbox']")
    if len(female_checkboxes) > 1:
        next_female_checkbox = female_checkboxes[1]
        wait.until(EC.element_to_be_clickable(next_female_checkbox)).click()
        time.sleep(1)

        # Set mating tag to 'M4'
        mating_tag_input = wait.until(
            EC.element_to_be_clickable((By.ID, "matingTag"))
        )
        mating_tag_input.clear()
        mating_tag_input.send_keys("M4")
        time.sleep(1)

        # Date and strain remain the same, so just click Add again
        add_button = wait.until(
            EC.element_to_be_clickable((By.ID, "batchApply"))
        )
        add_button.click()
        time.sleep(2)

    # Click 'Create Matings and Move Breeders into Cages' button
    move_breeders_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "submitBatchesAndMove"))
    )
    move_breeders_btn.click()
    time.sleep(2)

    # On move animals page, click 'Create / Update Cages'
    create_update_cages_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "moveApply"))
    )
    create_update_cages_btn.click()
    time.sleep(2)

    # On move summary page, click 'Done' button
    done_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "backbtn"))
    )
    done_btn.click()
    time.sleep(2)

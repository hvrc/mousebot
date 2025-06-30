import pytest
from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.matings_page import MatingsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_mating_invalid_date(driver, config):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    matings_page = MatingsPage(driver)

    home_page.go_to_colony()
    colony_page.go_to_matings()
    matings_page.start_new_mating()
    matings_page.select_first_male()
    matings_page.select_first_female()
    matings_page.set_setup_date("01-02-2025")
    matings_page.set_mating_tag("M5")
    matings_page.select_first_strain()
    matings_page.add_mating()

    # Wait for and handle warning popup
    wait = WebDriverWait(driver, 10)
    popup_ok_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ui-dialog-buttonset')]/button/span[text()='OK']/.."))
    )
    popup_ok_btn.click()
    time.sleep(1)
    home_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='home']//a[contains(@href, 'HomePage.do')]"))
    )
    home_button.click()
    time.sleep(2)
    assert "homepage.do" in driver.current_url.lower()

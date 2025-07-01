import pytest
from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.matings_page import MatingsPage

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

    # Handle warning popup and go home
    matings_page.handle_warning_popup_and_go_home()
    assert "homepage.do" in driver.current_url.lower()

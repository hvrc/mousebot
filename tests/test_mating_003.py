import pytest
from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.matings_page import MatingsPage

def test_mating_workflow(driver, config):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    matings_page = MatingsPage(driver)

    # Verify on home page
    assert "homepage.do" in driver.current_url.lower(), "Not on home page!"

    # Navigate to Colony module and Matings tab
    home_page.go_to_colony()
    colony_page.go_to_matings()

    # Start new mating workflow
    matings_page.start_new_mating()
    matings_page.select_first_male()
    matings_page.select_first_female()
    matings_page.set_setup_date("02-01-2025")
    matings_page.set_mating_tag("M3")
    matings_page.select_first_strain()
    matings_page.add_mating()

    # Add a second mating with next available female if present
    matings_page.add_second_mating_if_available("M4")

    # Move breeders and create/update cages
    matings_page.move_breeders()
    matings_page.create_update_cages()
    matings_page.done()

    # Go back home by pressing home button (now via POM)
    matings_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

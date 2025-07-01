import pytest
import time
from pages.login_page import LoginPage
from pages.litters_page import LittersPage
from pages.matings_page import MatingsPage
from pages.animals_page import AnimalsPage
from pages.strains_page import StrainsPage

def test_reset_001(driver, config):
    login_page = LoginPage(driver)
    litters_page = LittersPage(driver)
    matings_page = MatingsPage(driver)
    animals_page = AnimalsPage(driver)
    strains_page = StrainsPage(driver)

    # Navigate to colony module
    login_page.navigate_to_colony()

    # Litters Section
    litters_page.go_to_litters_tab()
    litters_page.delete_all_litters()

    # Matings Section
    matings_page.go_to_matings_tab()
    matings_page.disband_and_deactivate_all_matings()

    # Animals Section
    animals_page.go_to_animals_tab()
    animals_page.delete_all_animals()

    # Strains Section
    strains_page.go_to_strains_tab()
    strains_page.delete_all_strains()

    # Go home
    strains_page.go_home()
    assert "homepage.do" in driver.current_url.lower()
from pages.home_page import HomePage
from pages.litters_page import LittersPage
from pages.matings_page import MatingsPage
from pages.animals_page import AnimalsPage
from pages.strains_page import StrainsPage
from pages.colony_page import ColonyPage

def test_reset_001(driver):
    home_page = HomePage(driver)
    litters_page = LittersPage(driver)
    matings_page = MatingsPage(driver)
    animals_page = AnimalsPage(driver)
    strains_page = StrainsPage(driver)
    colony_page = ColonyPage(driver)
    home_page.go_to_colony()
    litters_page.go_to_litters_tab()
    litters_page.delete_all_litters()
    colony_page.go_to_matings()
    matings_page.disband_and_deactivate_all_matings()
    colony_page.go_to_animals_tab()
    animals_page.delete_all_animals()
    colony_page.go_to_strains()
    strains_page.delete_all_strains()
    colony_page.go_home()
    assert "homepage.do" in driver.current_url.lower()
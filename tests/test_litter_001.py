from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.litters_page import LittersPage

DOB = "03-01-2025"

def test_litter_001(driver):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    litters_page = LittersPage(driver)
    home_page.go_to_colony()
    colony_page.go_to_matings()
    litters_page.select_first_mating()
    litters_page.click_new_litter()
    litters_page.enter_dob(DOB)
    litters_page.create_litters()
    litters_page.confirm_popup()
    litters_page.go_to_litters_tab()
    litters_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

from pages.home_page import HomePage
from pages.litters_page import LittersPage

MALE_PUPS_COUNT = "1"

def test_pups_001(driver):
    home_page = HomePage(driver)
    litters_page = LittersPage(driver)
    home_page.go_to_colony()
    litters_page.go_to_litters_tab()
    litters_page.select_first_litter()
    litters_page.click_add_pups()
    litters_page.select_first_litter_pups()
    litters_page.select_males_dropdown(MALE_PUPS_COUNT)
    litters_page.click_submit_pups()
    litters_page.confirm_popup()
    litters_page.go_to_litters_tab()
    litters_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

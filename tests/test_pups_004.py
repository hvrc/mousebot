from pages.home_page import HomePage
from pages.litters_page import LittersPage

TAG_PREFIX = "B"
TAG_START_INDEX = 1

def test_pups_004(driver):
    home_page = HomePage(driver)
    litters_page = LittersPage(driver)
    home_page.go_to_colony()
    litters_page.go_to_litters_tab()
    litters_page.select_first_litter()
    litters_page.click_wean_litters()
    litters_page.select_first_pup_wean()
    litters_page.enter_physical_tag(TAG_PREFIX, TAG_START_INDEX)
    litters_page.click_apply_button()
    litters_page.click_wean_move_button()
    litters_page.click_create_update_cages_button()
    litters_page.click_done_button()
    litters_page.go_to_animals_tab()
    litters_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

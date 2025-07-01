from pages.home_page import HomePage
from pages.litters_page import LittersPage

TAG_PREFIX = "B"
TAG_START_INDEX = 1

def test_pups_004(driver, config):
    home_page = HomePage(driver)
    litters_page = LittersPage(driver)

    # 1. Go to Colony module
    home_page.go_to_colony()
    # 2. Go to Litters tab
    litters_page.go_to_litters_tab()
    # 3. Select first available litter checkbox
    litters_page.select_first_litter()
    # 4. Click on wean litters button
    litters_page.click_wean_litters()
    # 5. Select first available pup checkbox in weaning table
    litters_page.select_first_pup_wean()
    # 6. Enter physical tag B 1
    litters_page.enter_physical_tag(TAG_PREFIX, TAG_START_INDEX)
    # 7. Click apply
    litters_page.click_apply_button()
    # 8. Click wean pups and move weanlings into cages button
    litters_page.click_wean_move_button()
    # 9. Click create/update cages button
    litters_page.click_create_update_cages_button()
    # 10. Click done button
    litters_page.click_done_button()
    # 11. Click on animals tab
    litters_page.go_to_animals_tab()
    # 12. Click on home button
    litters_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

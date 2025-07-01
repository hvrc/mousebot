from pages.home_page import HomePage
from pages.litters_page import LittersPage
from pages.colony_page import ColonyPage

# 1. From Home Page, click on modules icon and navigate to "Colony" module.
# 2. Navigate to Litters tab.
# 3. Select a litter record.
# 4. Click "Wean Litters" button.
# 5. Select pups to be weaned.
# 7. Set Physical Tag.
# 8. Click "Apply"
# 9. Click "Wean Pups and Move Weanlings into Cages" button
# 10. Verify data on Move Animals page, click "Create/Update Cages" button.
# 11. Verify data on Move Summary page, click "Done" button.

TAG_PREFIX = "B"
TAG_START_INDEX = 1

def test_pups_004(driver):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
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
    colony_page.go_to_animals_tab()
    colony_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

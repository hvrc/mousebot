from pages.home_page import HomePage
from pages.litters_page import LittersPage
from pages.colony_page import ColonyPage

# 1. From Home Page, click on modules icon and navigate to "Colony" module.
# 2. Navigate to Litters tab.
# 3. Select litter.
# 4. Click "Add Pups" button.
# 5. Select litter.
# 6. Add number of males, females, unknown.
# 7. Click "Submit" button and "OK" on pop-up.

MALE_PUPS_COUNT = "1"

def test_pups_001(driver):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
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
    colony_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

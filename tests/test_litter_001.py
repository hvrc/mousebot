from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.matings_page import MatingsPage
from pages.litters_page import LittersPage

DOB = "03-01-2025"

def test_litter_001(driver, config):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    litters_page = LittersPage(driver)

    # 1. Go to Colony module
    home_page.go_to_colony()
    # 2. Go to Matings tab
    colony_page.go_to_matings()
    # 3. Select first available mating record's checkbox in jqGrid
    litters_page.select_first_mating()
    # 4. Click "New Litter" button
    litters_page.click_new_litter()
    # 5. Enter date of birth
    litters_page.enter_dob(DOB)
    # 6. Click "Create Litters" button
    litters_page.create_litters()
    # 7. Click "OK" on pop-up
    litters_page.confirm_popup()
    # 8. Navigate to Litters tab before going home
    litters_page.go_to_litters_tab()
    # 9. Redirect to home page
    litters_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

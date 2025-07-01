from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.matings_page import MatingsPage

# 1. From Home Page, click on modules icon and navigate to "Colony" module.
# 2. Navigate to Matings tab.
# 3. Click "New Matings" button.
# 4. Select one male and one female, enter set up date, litter strain, mating tag.
# 5. Click "Add" button
# 6. Select second female with first male still selected, enter set up date, litter strain, mating tag.
# 7. Click "Add" button.
# 8. Click "Create Matings and Move Breeders into Cages" button.
# 9. Verify data on Move Animals page, click "Create/Update Cages" button.
# 10. Verify data on Move Summary page, click "Done" button.

SETUP_DATE = "02-01-2025"
MATING_TAG_1 = "M3"
MATING_TAG_2 = "M4"

def test_mating_003(driver):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    matings_page = MatingsPage(driver)
    assert "homepage.do" in driver.current_url.lower(), "Not on home page!"
    home_page.go_to_colony()
    colony_page.go_to_matings()
    matings_page.start_new_mating()
    matings_page.select_first_male()
    matings_page.select_first_female()
    matings_page.set_setup_date(SETUP_DATE)
    matings_page.set_mating_tag(MATING_TAG_1)
    matings_page.select_first_strain()
    matings_page.add_mating()
    matings_page.add_second_mating_if_available(MATING_TAG_2)
    matings_page.move_breeders()
    matings_page.create_update_cages()
    matings_page.done()
    matings_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

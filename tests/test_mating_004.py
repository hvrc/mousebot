from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.matings_page import MatingsPage
from utilities.screenshot import take_screenshot

SETUP_DATE = "01-02-2025"
MATING_TAG = "M5"
SCREENSHOT_NAME = "test_mating_004_warning"

def test_mating_004(driver, request):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    matings_page = MatingsPage(driver)
    home_page.go_to_colony()
    colony_page.go_to_matings()
    matings_page.start_new_mating()
    matings_page.select_first_male()
    matings_page.select_first_female()
    matings_page.set_setup_date(SETUP_DATE)
    matings_page.set_mating_tag(MATING_TAG)
    matings_page.select_first_strain()
    matings_page.add_mating()
    report_folder = getattr(request.node, '_report_folder', 'reports')
    take_screenshot(driver, output_dir=report_folder, name=SCREENSHOT_NAME)
    matings_page.handle_warning_popup_and_go_home()
    assert "homepage.do" in driver.current_url.lower()

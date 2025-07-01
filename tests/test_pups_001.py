import pytest
from pages.home_page import HomePage
from pages.colony_page import ColonyPage
from pages.litters_page import LittersPage
from selenium.webdriver.support.ui import Select
import time

def test_pups_001(driver, config):
    home_page = HomePage(driver)
    colony_page = ColonyPage(driver)
    litters_page = LittersPage(driver)

    # 1. Go to Colony module
    home_page.go_to_colony()
    # 2. Go to Litters tab
    litters_page.go_to_litters_tab()

    # 3. Select first available litter record's checkbox in jqGrid
    litters_page.select_first_litter()

    # 4. Click "Add Pups" button
    litters_page.click_add_pups()
    time.sleep(2)

    # 5. Select first available litter in pups jqGrid
    litters_page.select_first_litter_pups()
    time.sleep(1)

    # 6. Select 1 from male dropdown
    litters_page.select_males_dropdown("1")
    time.sleep(1)

    # 7. Click "Submit" button (id="addPups")
    litters_page.click_submit_pups()
    time.sleep(1)

    # 8. Handle popup OK button
    litters_page.confirm_popup()
    time.sleep(1)

    # 9. Click on Litters tab
    litters_page.go_to_litters_tab()
    time.sleep(2)

    # 10. Click on home button
    litters_page.go_home()
    assert "homepage.do" in driver.current_url.lower()

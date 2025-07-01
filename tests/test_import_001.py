import pytest
from pages.import_page import ImportPage

def test_import_workflow(driver, config):
    import_page = ImportPage(driver)
    assert "homepage" in driver.current_url.lower() or "home" in driver.current_url.lower()
    import_page.go_to_import()
    import_page.assert_on_import_page()
    import_page.check_errors()
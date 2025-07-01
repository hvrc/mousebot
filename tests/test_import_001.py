import os
from pages.home_page import HomePage
from pages.import_page import ImportPage

# 1. From Home Page, click on modules icon and navigate to "Colony" module.
# 2. From Colony module, click "Import" button in top right.
# 3. Optionally, click "Download Template with Test Data" hyperlink.
# 4. Click "Upload File" button.
# 5. Select either "Template with Test Data.xlsx" or any valid .xlsx file via file upload input.
# 6. Click "Check for Errors" button.
# 7. Verify no errors or warnings appear.
# 8. Click "Proceed to Import" button.

def test_import_001(driver, config):
    home_page = HomePage(driver)
    import_page = ImportPage(driver)
    assert "homepage" in driver.current_url.lower() or "home" in driver.current_url.lower()
    home_page.go_to_import()
    import_page.assert_on_import_page()
    data_file_name = config['import_data_file']
    data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data', data_file_name))
    import_page.upload_file(data_file)
    import_page.check_errors()
    import_page.proceed_with_import()
    import_page.confirm_import()
    import_page.close_import_tab_and_return()
    assert "homepage.do" in driver.current_url.lower()
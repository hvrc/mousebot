import os
from pages.import_page import ImportPage

def test_import_001(driver, config):
    import_page = ImportPage(driver)
    assert "homepage" in driver.current_url.lower() or "home" in driver.current_url.lower()
    import_page.go_to_import()
    import_page.assert_on_import_page()
    data_file_name = config['import_data_file']
    data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data', data_file_name))
    import_page.upload_file(data_file, )
    import_page.check_errors()
    import_page.proceed_with_import()
    import_page.confirm_import()
    import_page.close_import_tab_and_return()
    assert "homepage.do" in driver.current_url.lower()
from pages.import_page import ImportPage
import os

def test_import_001(driver, config, request):
    import_page = ImportPage(driver)
    assert "homepage" in driver.current_url.lower() or "home" in driver.current_url.lower()
    report_folder = getattr(request.node, '_report_folder', 'reports')
    import_page.go_to_import(report_folder=report_folder)
    import_page.assert_on_import_page()

    # Upload the file (filename from config only)
    data_file_name = config['import_data_file']
    data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data', data_file_name))
    import_page.upload_file(data_file, report_folder=report_folder)

    # Click the Check for Errors button
    import_page.check_errors()

    # Proceed with Import
    import_page.proceed_with_import(report_folder=report_folder)

    # Confirm Import
    import_page.confirm_import(report_folder=report_folder)

    # Close the import tab and switch back to the original tab
    import_page.close_import_tab_and_return(report_folder=report_folder)

    # Assert we are back on the home page
    assert "homepage.do" in driver.current_url.lower()
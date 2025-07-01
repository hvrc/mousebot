from pages.login_page import LoginPage

def test_login_001(driver, config):
    login_page = LoginPage(driver)
    # Navigate to login page
    login_page.go_to_login_page(config['url'])
    # Login
    login_page.login(config['username'], config['password'])
    # Assert on home page
    assert login_page.is_on_home_page()
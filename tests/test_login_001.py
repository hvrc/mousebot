from pages.login_page import LoginPage

def test_login_001(driver, config):
    login_page = LoginPage(driver)
    login_page.go_to_login_page(config['url'])
    login_page.login(config['username'], config['password'])
    assert login_page.is_on_home_page()
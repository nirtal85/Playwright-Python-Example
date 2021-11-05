from page_object.login_page import LoginPage

ex_url = "https://www.dasdsa.com/inventory.html"
ex_error_message = "Epic sadface: Username and password do not match any user in this service"


def test_valid_login(page):
    lp = LoginPage(page)
    lp.input_username("standard_user")
    lp.input_password("secret_sauce")
    lp.click_login_button()
    assert (page.url == ex_url)


def test_invalid_login(page):
    lp = LoginPage(page)
    lp.input_username("standard_user")
    lp.input_password("secret_sauce1")
    lp.click_login_button()
    assert (lp.get_error_message_text() == ex_error_message)

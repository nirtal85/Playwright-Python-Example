from page_object.login_page import LoginPage

ex_url = "https://www.dasdsa.com/inventory.html"
ex_error_message = "Epic sadface: Username and password do not match any user in this service"
ex_locked_out_user_message = "Epic sadface: Sorry, this user has been locked out."


def test_valid_login(page):
    lp = LoginPage(page)
    lp.input_username("standard_user")
    lp.input_password("secret_sauce")
    lp.click_login_button()
    assert page.url == ex_url, f"Expected url to be {ex_url} after a valid login, but got {page.url} instead"


def test_invalid_login(page):
    lp = LoginPage(page)
    lp.input_username("standard_user")
    lp.input_password("secret_sauce1")
    lp.click_login_button()
    assert lp.get_error_message_text() == ex_error_message, \
        f"Expected invalid login error message to be {ex_error_message}, but got {lp.get_error_message_text()} instead"


def test_locked_out_user(page):
    lp = LoginPage(page)
    lp.input_username("locked_out_user")
    lp.input_password("secret_sauce")
    lp.click_login_button()
    assert lp.get_error_message_text() == ex_locked_out_user_message, \
        f"Expected locked out user message to be {ex_locked_out_user_message}, " \
        f"but got {lp.get_error_message_text()} instead"

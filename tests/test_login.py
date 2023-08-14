import pytest

from pages.login_page import LoginPage

ex_url = "https://www.saucedemo.com/inventory.html"
ex_error_message = (
    "Epic sadface: Username and password do not match any user in this service"
)
ex_locked_out_user_message = "Epic sadface: Sorry, this user has been locked out."


class TestLogin:
    @pytest.fixture(autouse=True)
    # Instantiates Page Objects
    def setup(self, elements):
        self.login_page = LoginPage(elements)

    def test_valid_login(self, elements, page):
        self.login_page.login("standard_user", "secret_sauce")
        assert (
                page.url == ex_url
        ), f"Expected url to be {ex_url} after a valid login, but got {page.url} instead"

    def test_invalid_login(self, page, elements):
        self.login_page.login("standard_user", "secret_sauce1")
        assert self.login_page.get_error_message_text() == ex_error_message, (
            f"Expected invalid login error message to be {ex_error_message},"
            f" but got {self.login_page.get_error_message_text()} instead "
        )

    def test_locked_out_user(self, page, elements):
        self.login_page.login("locked_out_user", "secret_sauce")
        assert self.login_page.get_error_message_text() == ex_locked_out_user_message, (
            f"Expected locked out user message to be {ex_locked_out_user_message}, "
            f"but got {self.login_page.get_error_message_text()} instead"
        )

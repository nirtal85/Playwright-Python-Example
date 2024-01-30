import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

ex_url = "https://www.saucedemo.com/inventory.html"
ex_error_message = (
    "Epic sadface: Username and password do not match any user in this service"
)
ex_locked_out_user_message = "Epic sadface: Sorry, this user has been locked out."


class TestLogin:
    @pytest.fixture(autouse=True)
    # Instantiates Page Objects
    def setup(self, page: Page):
        self.login_page = LoginPage(page)

    def test_valid_login(self, page: Page):
        self.login_page.login("standard_user", "secret_sauce")
        expect(page).to_have_url(ex_url)

    def test_invalid_login(self, page: Page):
        self.login_page.login("standard_user", "secret_sauce1")
        expect(self.login_page.error_message).to_have_text(ex_error_message)

    @pytest.mark.devRun
    def test_locked_out_user(self, page: Page):
        self.login_page.login("locked_out_user", "secret_sauce")
        expect(self.login_page.error_message).to_have_text(ex_locked_out_user_message)
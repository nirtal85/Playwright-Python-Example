import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)
    # Instantiates Page Objects
    def setup(self, page: Page):
        self.login_page = LoginPage(page)

    def test_valid_login(self, base_url, page: Page):
        self.login_page.login("standard_user", "secret_sauce")
        expect(page).to_have_url(f"{base_url}inventory.html")

    def test_invalid_login(self, page: Page):
        self.login_page.login("standard_user", "secret_sauce1")
        expect(self.login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service"
        )

    @pytest.mark.devRun
    def test_locked_out_user(self, page: Page):
        self.login_page.login("locked_out_user", "secret_sauce")
        expect(self.login_page.error_message).to_have_text(
            "Epic sadface: Sorry, this user has been locked out."
        )

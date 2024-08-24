import pytest
from playwright.sync_api import Page, expect

from enums.User import User


class TestCheckout:

    @pytest.mark.parametrize(
        "browser_context_args", [User.STANDARD_USER], indirect=True
    )
    def test_checkout_counter(self, browser_context_args, page: Page):
        page.evaluate("localStorage.setItem('cart-contents', '[4,0]');")
        page.reload()
        expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("2")

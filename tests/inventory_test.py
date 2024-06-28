import pytest
from playwright.sync_api import Page, expect

from enums.User import User


class TestInventory:

    @pytest.mark.parametrize(
        "browser_context_args", [User.STANDARD_USER], indirect=True
    )
    def test_inventory_page(self, browser_context_args, page: Page):
        expect(page.locator("//span[@class='title']")).to_have_text("Products")

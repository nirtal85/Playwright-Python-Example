import pytest
from playwright.sync_api import Page


class TestInventory:

    @pytest.mark.parametrize("browser_context_args", ["standard_user"], indirect=True)
    def test_inventory_page(self, browser_context_args, page: Page):
        assert page.inner_text("//span[@class='title']") == "Products"

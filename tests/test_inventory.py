import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestInventory:

    @pytest.fixture(autouse=True)
    # Instantiates Page Objects
    def setup(self, elements):
        self.login_page = LoginPage(elements)

    @allure.title("Test item addition to cart")
    @allure.description(
        "Assert that when user clicks on Add to cart button, the Remove to cart button is displayed instead")
    def test_add_to_cart(self, page):
        item_name = "Sauce Labs Backpack"
        ip = InventoryPage(page)
        ip.add_item_to_cart(item_name)
        assert ip.is_remove_button_displayed(), \
            "Expected Remove button to be displayed after item addition to cart, but it was not"

from selenium.webdriver.support.ui import Select


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.__CART_BUTTON = self.page.locator("#shopping_cart_container")
        self.__SORT_FIELD = self.page.locator("[data-test='product_sort_container']")
        self.__HAMBURGER_MENU_BUTTON = self.page.locator("#react-burger-menu-btn")
        self.__ITEMS_LIST = self.page.locator(".inventory_list>div")

    def click_cart(self):
        self.__CART_BUTTON.click()

    def click_hamburger_menu(self):
        self.__HAMBURGER_MENU_BUTTON.click()

    def get_item_price(self, item_name):
        for i in self.__ITEMS_LIST:
            if item_name == i.text_content():
                return i.locator(".inventory_item_price").text_content().split("$")[1]

    def get_all_prices(self):
        aux_list = []
        for i in self.__ITEMS_LIST:
            aux_list.append(i.locator(".inventory_item_price").text_content().split("$")[1])
        return aux_list

    def add_item_to_cart(self, item_name):
        for i in self.__ITEMS_LIST:
            if item_name == i.text_content():
                i.locator("data-test='add-to-cart-sauce-labs-backpack'").click()
                break

    def select_sort_according_to_property(self, prop):
        select = Select(self.__SORT_FIELD)

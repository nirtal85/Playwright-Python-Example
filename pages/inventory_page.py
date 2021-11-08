import allure


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.__CART_BUTTON = self.page.locator("#shopping_cart_container")
        self.__SORT_FIELD = self.page.locator("[data-test='product_sort_container']")
        self.__HAMBURGER_MENU_BUTTON = self.page.locator("#react-burger-menu-btn")
        self.__ITEMS_LIST = self.page.locator(".inventory_list>div")

    @allure.step("Click on cart icon")
    def click_cart(self):
        self.__CART_BUTTON.click()

    @allure.step("Click Hamburger menu")
    def click_hamburger_menu(self):
        self.__HAMBURGER_MENU_BUTTON.click()

    @allure.step("Get price for item {item_name}")
    def get_item_price(self, item_name):
        for i in self.__ITEMS_LIST:
            if item_name == i.text_content():
                return i.locator(".inventory_item_price").text_content().split("$")[1]

    @allure.step("Get all items prices")
    def get_all_prices(self):
        aux_list = []
        for i in self.__ITEMS_LIST:
            aux_list.append(i.locator(".inventory_item_price").text_content().split("$")[1])
        return aux_list

    @allure.step("Get all items names")
    def get_all_items_names(self):
        aux_list = []
        for i in self.__ITEMS_LIST:
            aux_list.append(i.locator(".inventory_item_name").text_content())
        return aux_list

    @allure.step("Check if 'Remove' button is displayed")
    def is_remove_button_displayed(self):
        return self.page.is_visible("data-test='remove-sauce-labs-backpack'")

    @allure.step("Add item {item_name} to cart")
    def add_item_to_cart(self, item_name):
        for i in self.__ITEMS_LIST:
            if item_name == i.text_content():
                i.locator("data-test='add-to-cart-sauce-labs-backpack'").click()
                break

    @allure.step("Sort items according to {property_name}")
    def select_sorting_according_to_property(self, property_name):
        if property_name == "name_asc":
            self.__SORT_FIELD.select_option(value="az")
        elif property_name == "name_desc":
            self.__SORT_FIELD.select_option(value="za")
        elif property_name == "price_asc":
            self.__SORT_FIELD.select_option(value="lohi")
        elif property_name == "price_desc":
            self.__SORT_FIELD.select_option(value="hilo")

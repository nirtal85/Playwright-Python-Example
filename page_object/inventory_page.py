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


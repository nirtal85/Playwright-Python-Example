class LoginPage:

    def __init__(self, page):
        self.page = page
        self.__USER_NAME_FIELD = self.page.locator("[data-test='username']")
        self.__PASSWORD_FIELD = self.page.locator("[data-test='password']")
        self.__LOGIN_BUTTON = self.page.locator("[data-test='login-button']")
        self.__ERROR_MESSAGE = self.page.locator("[data-test='error']")

    def input_username(self, username):
        self.__USER_NAME_FIELD.type(username)

    def input_password(self, password):
        self.__PASSWORD_FIELD.type(password)

    def click_login_button(self):
        self.__LOGIN_BUTTON.click()

    def get_error_message_text(self):
        return self.__ERROR_MESSAGE.text_content()

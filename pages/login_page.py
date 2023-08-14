import typing
from dataclasses import dataclass

import allure
from playwright.sync_api import Locator


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Login page behavior")
@dataclass
class LoginPage:
    elements: typing.Dict[str, Locator]

    @allure.step("Login with username {username} and password {password}")
    def login(self, username, password):
        self.elements.get("user_name_field").type(username)
        self.elements.get("password_field").type(password)
        self.elements.get("login_button").click()

    @allure.step("Get error message")
    def get_error_message_text(self):
        return self.elements.get("error_message").text_content()

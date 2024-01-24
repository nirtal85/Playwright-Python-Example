from dataclasses import dataclass

import allure
from playwright.sync_api import Page


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Login page behavior")
@dataclass
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    @allure.step("Login with username {username} and password {password}")
    def login(self, username, password):
        self.user_name_field.type(username)
        self.password_field.type(password)
        self.login_button.click()

    @allure.step("Get error message")
    def get_error_message_text(self):
        return self.error_message.text_content()

import typing
from dataclasses import dataclass


@dataclass
class LoginPage:
    elements: typing.Dict

    def login(self, username, password):
        self.elements.get("user_name_field").type(username)
        self.elements.get("password_field").type(password)
        self.elements.get("login_button").click()

    def get_error_message_text(self):
        return self.elements.get("error_message").text_content()

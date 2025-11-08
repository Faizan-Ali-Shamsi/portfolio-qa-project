from selenium.webdriver.common.by import By
from Pages.Base import BasePage


class LoginPage(BasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    submit_button = (By.ID, "submit")
    error_message = (By.ID, "error")

    def login(self, username, password):
        self.type_text(self.username_input, username)
        self.type_text(self.password_input, password)
        self.click(self.submit_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

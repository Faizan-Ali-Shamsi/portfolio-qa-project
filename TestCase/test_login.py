from Pages.loginpage import LoginPage
import json
import pytest


with open("Data/testdata.json") as f:
    data = json.load(f)


class Test:
    @pytest.mark.parametrize("data", data.values())
    def test_login(self, setup, data):
        driver = setup
        login_page = LoginPage(driver)

        username = data["username"]
        password = data["password"]

        login_page.login(username, password)

        try:
            if username == "student" and password == "Password123":
                assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url

            elif username != "student":
                assert "Your username is invalid!" in login_page.get_error_message()

            else:
                assert "Your password is invalid!" in login_page.get_error_message()
        except AssertionError:
            driver.save_screenshot(f"Screenshots/login_fail_{username}.png")
            raise

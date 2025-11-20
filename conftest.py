from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def setup(browser):
    if browser == "chrome":
        d = webdriver.Chrome()
    elif browser == "firefox":
        d = webdriver.Firefox()
    elif browser == "edge":
        d = webdriver.Edge()
    else:
        raise ValueError("Please enter a valid browser name: chrome, firefox, edge")
    d.get("https://practicetestautomation.com/practice-test-login/")
    d.maximize_window()
    yield d
    d.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome",
                     help="Browser to run test.")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser").lower()

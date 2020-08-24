import allure
import pytest

from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.main_page import HabrMainPage
from Pages.profile_page import ProfilePage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Testing browser')
    parser.addoption("--selenoid", action="store", default="localhost")


@pytest.fixture
def login_page(browser):
    page = LoginPage(browser)
    page.go_to()
    return page


@pytest.fixture
def main_page(browser):
    page = HabrMainPage(browser)
    page.go_to()
    return page


@pytest.fixture
def profile_page(browser):
    page = ProfilePage(browser)
    page.go_to()
    return page


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    selenoid = '192.168.97.157'

    executor_url = f"http://{selenoid}:4444/wd/hub"

    caps = {
            "browserName": browser,
            "version": "83.0",
            "enableVnc": True,
            "enableVideo": True,
            "enableLog": True,
            "screenResolution": "1280x720",
            "name": request.node.name,
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
            }

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)

    allure.attach(name=driver.session_id,
                  body=str(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)

    yield driver
    driver.quit()

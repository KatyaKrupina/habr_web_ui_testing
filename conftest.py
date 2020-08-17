import datetime
import logging

import allure
import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, DesiredCapabilities
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, filename="Logs/test.log")
from Pages.base import BasePage


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='Chrome',
        help='Testing browser'
    )
    parser.addoption(
        '--url',
        default='http://localhost/',
        help='Testing url'
    )


@pytest.fixture
def browser_name(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def url(request):
    return request.config.getoption('--url')


# @pytest.fixture()
# def catalog_url():
#     url = 'http://localhost/index.php?route=product/category&path=20'
#     return url


# @pytest.fixture()
# def product_url():
#     url = 'http://localhost/index.php?route=product/product&path=57&product_id=49'
#     return url
#
#
# @pytest.fixture()
# def login_url():
#     url = 'http://localhost/index.php?route=account/login'
#     return url
#
#
# @pytest.fixture()
# def admin_url():
#     url = 'http://localhost/admin/'
#     return url
#
#
# @pytest.fixture()
# def admin_page(browser):
#     logger.info('Go to admin page')
#     page = AdminLoginPage(browser)
#     page.go_to()
#     return page
#
#
@pytest.fixture()
def main_page(browser):
    # logger.info('Go to main page')
    page = BasePage(browser)
    page.go_to()
    return page
#
#
# @pytest.fixture()
# def tablets_page(browser):
#     logger.info('Go to tablets page')
#     page = TabletsPage(browser)
#     page.go_to()
#     return page


@pytest.fixture()
def browser(browser_name):
    driver = ''
    if browser_name == 'Chrome':
        caps = DesiredCapabilities.CHROME
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('w3c', False)
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        driver.implicitly_wait(5)

    elif browser_name == 'Firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)

    elif browser_name == 'Safari':
        driver = webdriver.Safari()
        driver.implicitly_wait(5)

    else:
        pass

    allure.attach(name=driver.session_id,
                  body=str(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)

    yield driver
    driver.quit()
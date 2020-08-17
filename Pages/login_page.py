import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from .base import BasePage
from .selectors import MainPage


class LoginPage(BasePage):
    username = (By.ID, 'email_field')
    password = (By.ID, 'password_field')
    submit_button = (By.NAME, 'go')

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://account.habr.com/login/"

    def _set_username_(self, name):
        with allure.step("Enter name {}".format(name)):
            self.find_element(locator=self.username).clear()
            self.find_element(locator=self.username).send_keys(name)

    def _set_password_(self, password):
        with allure.step("Enter password {}".format(password)):
            self.find_element(locator=self.password).clear()
            self.find_element(locator=self.password).send_keys(password)

    def login(self, username, password):
        with allure.step("Logging to admin page"):
            self._set_username_(username)
            self._set_password_(password)
            self.find_element(locator=self.submit_button).click()

    def logout(self):
        with allure.step("Click logout button"):
            self.wait_for_element(AdminPage.LOGOUT).click()
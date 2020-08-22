import os

from selenium.webdriver.common.by import By

from Pages.base import BasePage
from Pages.login_page import LoginPage
from Pages.selectors import MainPage, Profile


class ProfilePage(LoginPage):
    user = (os.getenv('HABR_USER'))

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f'https://habr.com/ru/users/{self.user}/'

    def login_profile(self):
        self.find_element(MainPage.LOGIN).click()
        self.login(os.getenv('HABR_LOGIN'), os.getenv('HABR_PASS'))

    #todo allure
    def show_profile(self):
        self.find_element(Profile.USER_SETTINGS).click()
        self.find_element(Profile.USER_PROFILE).click()
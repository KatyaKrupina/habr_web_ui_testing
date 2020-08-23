import os

import allure

from Pages.login_page import LoginPage
from Pages.selectors import MainPage, Profile, Subscribe


@allure.feature('Profile Page')
class ProfilePage(LoginPage):
    user = (os.getenv('HABR_USER'))

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f'https://habr.com/ru/users/{self.user}/'

    def login_profile(self):
        with allure.step('Login profile'):
            self.find_element(MainPage.LOGIN).click()
            self.login(os.getenv('HABR_LOGIN'), os.getenv('HABR_PASS'))

    def show_profile(self):
        with allure.step('Opening profile'):
            self.find_element(Profile.USER_SETTINGS).click()
            self.find_element(Profile.USER_PROFILE).click()

    def show_settings(self):
        with allure.step('Showing profile settings'):
            self.login_profile()
            self.find_element(Profile.CHANGE_SETTINGS).click()

    def upload_new_avatar(self, new_avatar):
        with allure.step('Uploading new user pic'):
            dirname = os.path.dirname(__file__)
            file = os.path.join(dirname, new_avatar)
            input_file = self.find_element(Profile.INPUT_FILE)
            input_file.send_keys(file)
            self.find_element(Profile.SUBMIT_BTN).click()
            self.find_element(Profile.UPLOADED_FILE)

    def set_name(self, name: str):
        with allure.step('Setting new user name'):
            self.find_element(Profile.INPUT_TEXT).clear()
            self.find_element(Profile.INPUT_TEXT).send_keys(name)
            self.find_element(Profile.SUBMIT_BTN).click()
            self.find_element(Profile.UPDATED_MSG)

    def subscribe_hub(self):
        with allure.step('Subscribing hub'):
            self.find_elements(MainPage.NAVIGATION)[0].click()
            self.find_elements(Subscribe.SUBSCRIBE_BUTTON)[1].click()
            assert self.get_text_in_element(Subscribe.UNFOLLOW_BTN) == Subscribe.UNFOLLOW

    def unsubscribe_hub(self):
        with allure.step('Unsubscribing hub'):
            self.find_element(Subscribe.SUBSCRIBE).click()
            self.find_element(Subscribe.UNFOLLOW_HUB_BTN).click()
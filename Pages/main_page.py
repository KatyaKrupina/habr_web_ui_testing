from time import sleep

import allure
from selenium.webdriver.common.keys import Keys

from Pages.base import BasePage
from Pages.selectors import MainPage, SocialNetworks


@allure.feature('Habr Main Page')
class HabrMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_item(self, item_to_find):
        with allure.step(f'Searching {item_to_find}'):
            self.find_element(MainPage.SEARCH).click()
            self.find_element(MainPage.SEARCH_FIELD).send_keys(item_to_find)
            self.find_element(MainPage.SEARCH_FIELD).send_keys(Keys.RETURN)

    def go_to_youtube_habr_channel(self):
        with allure.step('Going to youtube habr channel'):
            self.find_element(SocialNetworks.YOUTUBE).click()
            self.switch_to_current_tab()

    def contact_by_telegram(self):
        with allure.step('Going to telegram contact page'):
            self.find_element(SocialNetworks.TELEGRAM).click()
            self.switch_to_current_tab()

    def change_to_english_language(self):
        with allure.step('Switching to english language'):
            self.find_element(MainPage.CHANGE_LANGUAGE).click()
            self.find_element(MainPage.ENG).click()
            self.find_element(MainPage.SUBMIT_BTN).click()
            sleep(1)

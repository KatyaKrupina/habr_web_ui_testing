import os
from time import sleep

from selenium.webdriver.common.keys import Keys

from Pages.selectors import MainPage, SocialNetworks, Profile, Subscribe


def test_title(main_page):
    title = main_page.get_title()
    assert title == MainPage.TITLE


def test_login(login_page):
    login_page.login(os.getenv('HABR_LOGIN'), os.getenv('HABR_PASS'))
    assert login_page.get_text_in_element(Profile.WELCOME) == Profile.WELCOME_TEXT


def test_logout(login_page):
    login_page.login(os.getenv('HABR_LOGIN'), os.getenv('HABR_PASS'))
    login_page.logout()
    assert login_page.get_text_in_element(MainPage.LOGIN_FORM) == 'Вход'


def test_search(main_page):
    main_page.find_element(MainPage.SEARCH).click()
    main_page.find_element(MainPage.SEARCH_FIELD).send_keys('Otus')
    main_page.find_element(MainPage.SEARCH_FIELD).send_keys(Keys.RETURN)
    main_page.find_element(Subscribe.HUBS).click()
    assert main_page.get_text_in_element(Subscribe.OTUS) == Subscribe.OTUS_DESCRIPTION


def test_go_to_youtube(main_page):
    main_page.find_element(SocialNetworks.YOUTUBE).click()
    main_page.switch_to_current_tab()
    title = main_page.get_title()
    assert title == SocialNetworks.YOUTUBE_CHANEL


def test_contact_by_telegram(main_page):
    main_page.find_element(SocialNetworks.TELEGRAM).click()
    main_page.switch_to_current_tab()
    title = main_page.get_title()
    assert title == SocialNetworks.TELEGRAM_CONTACT


def test_subscribe(profile_page):
    profile_page.login_profile()
    profile_page.find_elements(MainPage.NAVIGATION)[0].click()

    profile_page.find_elements(Subscribe.SUBSCRIBE_BUTTON)[1].click()

    assert profile_page.get_text_in_element(Subscribe.UNFOLLOW_BTN) == Subscribe.UNFOLLOW
    profile_page.show_profile()
    # profile_page.find_element(Profile.USER_SETTINGS).click()
    # profile_page.find_element(Profile.USER_PROFILE).click()

    assert profile_page.get_text_in_element(Subscribe.SUBSCRIBE) == '.NET'
    profile_page.find_element(Subscribe.SUBSCRIBE).click()
    profile_page.find_element(Subscribe.UNFOLLOW_HUB_BTN).click()


def test_change_avatar(profile_page):
    profile_page.login_profile()

    profile_page.find_element(Profile.CHANGE_SETTINGS).click()

    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 'avatar.jpeg')

    input_file = profile_page.find_element(Profile.INPUT_FILE)
    input_file.send_keys(file)
    profile_page.find_element(Profile.SUBMIT_BTN).click()
    profile_page.find_element(Profile.UPLOADED_FILE)

    assert profile_page.get_text_in_element(Profile.DELETE_AVATAR_BTN) == Profile.DELETE
    profile_page.find_element(Profile.DELETE_AVATAR_BTN).click()


def test_change_name(profile_page):
    profile_page.login_profile()

    profile_page.find_element(Profile.CHANGE_SETTINGS).click()
    profile_page.find_element(Profile.INPUT_TEXT).clear()
    profile_page.find_element(Profile.INPUT_TEXT).send_keys(Profile.USER_NAME)
    profile_page.find_element(Profile.SUBMIT_BTN).click()
    profile_page.find_element(Profile.UPDATED_MSG)
    profile_page.show_profile()

    # profile_page.find_element(Profile.USER_SETTINGS).click()
    # profile_page.find_element(Profile.USER_PROFILE).click()
    assert profile_page.get_text_in_element(Profile.USERNAME) == Profile.USER_NAME


def test_change_language(main_page):
    main_page.find_element(MainPage.CHANGE_LANGUAGE).click()
    main_page.find_element(MainPage.ENG).click()
    main_page.find_element(MainPage.SUBMIT_BTN).click()
    sleep(1)
    assert main_page.get_text_in_element(MainPage.HEADER) == MainPage.HEADER_ENG






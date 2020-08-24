import os
import allure

from Pages.selectors import MainPage, SocialNetworks, Profile, Subscribe


@allure.feature('Change habr settings')
@allure.title('Set english language')
def test_change_language(main_page):
    main_page.change_to_english_language()
    assert main_page.get_text_in_element(MainPage.HEADER) == MainPage.HEADER_ENG


@allure.feature('Change profile settings')
@allure.title('Subscribe channel')
def test_subscribe(profile_page):
    profile_page.login_profile()
    profile_page.subscribe_hub()
    profile_page.show_profile()
    assert profile_page.get_text_in_element(Subscribe.SUBSCRIBE) == '.NET'
    profile_page.unsubscribe_hub()


@allure.feature('Change profile settings')
@allure.title('Change user pic')
def test_change_avatar(profile_page):
    profile_page.show_settings()
    profile_page.upload_new_avatar('avatar.jpeg')
    assert profile_page.get_text_in_element(Profile.DELETE_AVATAR_BTN) == Profile.DELETE


@allure.feature('Change profile settings')
@allure.title('Change user name')
def test_change_name(profile_page):
    profile_page.show_settings()
    profile_page.set_name(Profile.USER_NAME)
    profile_page.show_profile()
    assert profile_page.get_text_in_element(Profile.USERNAME) == Profile.USER_NAME


@allure.feature('Habr Account')
@allure.title('Logging habr account')
def test_login(login_page):
    login_page.login(os.getenv('HABR_LOGIN'), os.getenv('HABR_PASS'))
    assert login_page.get_text_in_element(Profile.WELCOME) == Profile.WELCOME_TEXT


@allure.feature('Habr Account')
@allure.title('Logout habr account')
def test_logout(login_page):
    login_page.login(os.getenv('HABR_LOGIN'), os.getenv('HABR_PASS'))
    login_page.logout()
    assert login_page.get_text_in_element(MainPage.LOGIN_FORM) == 'Вход'


@allure.feature('Social Networks')
@allure.title('Open youtube channel')
def test_go_to_youtube(main_page):
    main_page.go_to_youtube_habr_channel()
    title = main_page.get_title()
    assert title == SocialNetworks.YOUTUBE_CHANEL


@allure.feature('Social Networks')
@allure.title('Contact by telegram')
def test_contact_by_telegram(main_page):
    main_page.contact_by_telegram()
    title = main_page.get_title()
    assert title == SocialNetworks.TELEGRAM_CONTACT


@allure.feature('Habr main page')
@allure.title('Checking title')
def test_title(main_page):
    title = main_page.get_title()
    assert title == MainPage.TITLE


@allure.feature('Search')
@allure.title('Searching item')
def test_search(main_page):
    main_page.search_item('Otus')
    main_page.find_element(MainPage.HUBS).click()
    assert main_page.get_text_in_element(Subscribe.OTUS) == Subscribe.OTUS_DESCRIPTION


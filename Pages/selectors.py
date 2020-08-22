from selenium.webdriver.common.by import By


class MainPage:
    TITLE = 'Лучшие публикации за сутки / Хабр'
    LOGIN = By.ID, 'login'
    LOGOUT = By.CSS_SELECTOR, '[class="button button_icon button_outline button_logout"]'
    LOGIN_FORM = By.CSS_SELECTOR, '[class="shadow-box__title"]'
    CHANGE_LANGUAGE = By.CSS_SELECTOR, '[class="footer__link js-show_lang_settings"]'
    ENG = By.CSS_SELECTOR, '[for="hl_langs_en"]'
    SUBMIT_BTN = By.CSS_SELECTOR, '[class="btn btn_blue btn_huge btn_full-width js-popup_save_btn"]'
    HEADER = By.CSS_SELECTOR, '[class="page-header page-header_110 "]'
    SEARCH = By.ID, 'search-form-btn'
    SEARCH_FIELD = By.ID, 'search-form-field'
    HEADER_ENG = 'All streams'
    NAVIGATION = By.CSS_SELECTOR, '[class="nav-links__item"]'


class Subscribe:
    HUBS = By.CSS_SELECTOR, '[title="Хабы и компании: 1"]'
    OTUS = By.CSS_SELECTOR, '[class="list-snippet__title-link"]'
    SUBSCRIBE_BUTTON = By.CSS_SELECTOR, '[class="subscribe-button subscribe-button_medium hub-info__subscribe-button"]'
    SUBSCRIBE = By.CSS_SELECTOR, '[class ="profile-section__user-hub profile-section__user-hub_cross"]'
    UNFOLLOW_HUB_BTN = By.CSS_SELECTOR, '[data-state="unfollow"]'
    UNFOLLOW_BTN = By.CSS_SELECTOR, '[subscribed="true"]'
    UNFOLLOW = 'Отписаться'
    OTUS_DESCRIPTION = 'Блог компании OTUS. Онлайн-образование'


class Profile:
    USER_NAME = 'Екатерина'
    USERNAME = By.CSS_SELECTOR, '[class ="user-info__fullname user-info__fullname_medium"]'
    USER = By.CSS_SELECTOR, '[class="user-info__name"]'
    CHANGE_SETTINGS = By.CSS_SELECTOR, '[class="btn btn_blue btn_x-large"]'
    INPUT_TEXT = By.CSS_SELECTOR, '[class="h-form-input__control"]'
    USER_SETTINGS = By.CSS_SELECTOR, '[class="btn btn_medium btn_navbar_user-dropdown"]'
    USER_PROFILE = By.CSS_SELECTOR, '[class ="dropdown__user-info user-info"]'
    UPDATED_MSG = By.CSS_SELECTOR, '[class="message message_successfull"]'
    INPUT_FILE = By.CSS_SELECTOR, '[class="form-fileupload__input form-fileupload__input_hidden"]'
    SUBMIT_BTN = By.CSS_SELECTOR, '[class="tm-button tm-button_submit h-form__submit-button"]'
    UPLOADED_FILE = By.CSS_SELECTOR, '[class="form-fileupload__image"]'
    DELETE_AVATAR_BTN = By.CSS_SELECTOR, '[class="form-fileupload__button"]'
    DELETE = 'Удалить'
    WELCOME = By.CSS_SELECTOR, '[class="welcome__text"]'
    WELCOME_TEXT = 'Это страница вашего аккаунта, который позволяет использовать одну учетную запись для сервисов ' \
                   'Хабр и Хабр Q&A. Он также упрощает авторизацию на сервисах Хабр Карьера и Хабр Фриланс. Чтобы ' \
                   'авторизоваться в один клик по кнопке «Войти с помощью Хабр Аккаунта», сначала добавьте этот ' \
                   'аккаунт в ключницу на этих сервисах.'


class SocialNetworks:
    YOUTUBE = By.CSS_SELECTOR, \
              '[class="social-icons__item-link social-icons__item-link_normal social-icons__item-link_youtube"]'
    TELEGRAM = By.CSS_SELECTOR, \
               '[class="social-icons__item-link social-icons__item-link_normal social-icons__item-link_telegram"]'
    YOUTUBE_CHANEL = 'Хабр - YouTube'
    TELEGRAM_CONTACT = 'Telegram: Contact @habr_com'

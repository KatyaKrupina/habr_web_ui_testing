from time import sleep


def test_r():
    print('hello')


def test_habr_title(browser):
    browser.get('https://habr.com/ru')
    title = browser.title
    sleep(3)
    assert title == 'Лучшие публикации за сутки / Хабр'


def test_habr_title1(main_page):
    title = main_page.get_title()
    assert title == 'Лучшие публикации за сутки / Хабр'


def test_change_language():
    pass


# habr_web_ui_testing
Тестирование web UI сайта habr.com

Тесты запускаются в Selenoid. \
Для запуска Selenoid должен быть установлен Docker. 
Команды для запуска:

    ./cm selenoid start
    ./cm selenoid-ui start  

Прогон тестов можно запустить через Dockerfile:

    docker build -t habr/tests .
    docker run --name test_run \
    -e HABR_LOGIN=$HABR_LOGIN \
    -e HABR_PASS=$HABR_PASS \
    -e HABR_USER=$HABR_USER \
    habr/tests

Переменные окружения:\
HABR_LOGIN - e-mail \
HABR_PASS - пароль \
HABR_USER - имя пользователя

Получение отчета allure:

    allure serve allure-reports
# Тестирование web UI сайта habr.com

Тесты запускаются в Selenoid. 
Инструкция для установки: https://aerokube.com/cm/latest/

## Прогон тестов
Прогон тестов можно запустить с помощью Pytest при настроенном окружении или через Dockerfile.

### Pytest

    pytest --alluredir=allure-results


### Docker

    docker build -t habr/tests .
    docker run --rm --name test_run \
    -e HABR_LOGIN=$HABR_LOGIN \
    -e HABR_PASS=$HABR_PASS \
    -e HABR_USER=$HABR_USER \
    -e SELENOID_HOST=$SELENOID_HOST \
    -v ${PWD}/allure-results:/app/allure-results \
    habr/tests

Переменные окружения:
- `HABR_LOGIN` - e-mail
- `HABR_PASS` - пароль
- `HABR_USER` - имя пользователя
- `SELENOID_HOST` - IP-адрес

## Получение отчета allure

Запустить контейнер с allure командой:

    docker run -p 5050:5050 -v ${PWD}/allure-results:/app/allure-results 
    frankescobar/allure-docker-service

Посмотреть отчет по ссылке:

    http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html
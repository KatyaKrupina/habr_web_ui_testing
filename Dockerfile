# Установка базового образа
FROM python:3.6

# Установка рабочей директории
WORKDIR /app

# Копирование файлов из текущей директории в директорию контейнера
COPY . .

# Выполнение необходимых команд
RUN pip install -U pip
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app

# Запуск тестов
CMD ["pytest", "--alluredir", "allure-reports"]
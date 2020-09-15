# Установка базового образа
FROM python:3.6

# Установка рабочей директории
WORKDIR /app

# Копирование requirements
COPY requirements.txt requirements.txt

# Установка зависимостей
RUN pip install -U pip
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app

# Копирование файлов из текущей директории в директорию контейнера
COPY . .

# Запуск тестов
CMD ["pytest", "--alluredir", "allure-results"]

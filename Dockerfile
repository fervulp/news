# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:latest
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app/backend

# Копирует все файлы из нашего локального проекта в контейнер
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt 


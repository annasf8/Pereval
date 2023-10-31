# Проект REST API для туристических перевалов.
### Описание:
По заданию необходимо усовершенствовать  REST API для ведения базы горных перевалов, которая пополняется туристами.
1. Реализованы методы API POST/submitData для добавления туристом информации о новом перевале; GET /submitData/<id> — получение одной записи о перевале по ее id, в том числе статус модерации; PATCH /submitData/<id> — редактирование существующей записи, если она еще не поступила в работу модератору, а также GET /submitData/?user__email=<email> — список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
2. Добавлен визуальный интерфейс Swagger.
###  Параметры реализации:
1.При подготовке проекта использована база данных PostgreSQL, установка командой '''pip install psycopg2''', порт, логин, пароль и путь к базе данных берется из переменных окружения с использваонием библиотеки dotenv: '''pip install python-dotenv'''
2.В файле requirements.txt приведен список внешних зависимостей, который формируется командoй '''pip freeze > requirements.txt'''
3. В настоящее время ведется работа над покрытием кода тестами и развертываем приложения на хостинге.
### Как работать с API:
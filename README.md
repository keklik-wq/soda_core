## Работа с Clickhouse
1. Установить [Docker Desktop](https://www.docker.com/products/docker-desktop/) и [DBeaver](https://dbeaver.io/download/)
2. Перейти в папку infra `cd ./infra`
3. Запустить контейнер с Clickhouse командой `docker-compose up -d`
4. Подключиться к Clickhouse с помощью DBeaver:
    - Тип подключения: Clickhouse
    - Хост: localhost
    - База данных: datamart_layer
    - Имя пользователя: admin
    - Пароль: admin
5. Выполнить скрипт `ddl.sql` в DBeaver для создания слоя данных


## Data Quality (Soda Core)
1. Установить [Python 3.11](https://www.python.org/downloads/release/python-3118/)
2. Проинициализировать venv (или через UI редактора кода) 
`python 3 -m venv .venv`
3. Установить необходимые библиотеки Python
`pip install -r requirements.txt`
4. Перейти в папку soda-demo `cd ./soda`
5. Протестировать соединение с Clickhouse командой `soda test-connection -d dwh -c configuration.yml`
6. Запустить data quality проверки командой `soda scan -d dwh -c configuration.yml dwh.yml`


## Дополнительные ссылки
* [Список доступных проверок в Soda Core](https://docs.soda.io/soda-cl/metrics-and-checks.html#list-of-sodacl-metrics-and-checks)

## Команды 
soda scan -V -d dwh -c configuration.yml dwh.yml
# TEST REST API
REST API позволяет сохранять, получать и модифицировать объекты.
Также имется возможность спроскировать api-метод (url: api/proxy) с кэшированием устаревающим
по времени и по количеству запросов. В качестве кэш-хранилища используется Redis.
Переменные, которые определяют максимальное количество запросов, после которых кэш устаревает
и максимальное время жизни кэша задаются в файле .env.


## Зависимости
- `python 3.8`
- всё из `requirements.txt`


## Запуск через Docker
- создать .env файл в корне проекта. Содержимое .env-файла представлено в .env.example
- установить docker и docker-compose
  - гайд по установке docker: https://docs.docker.com/engine/install/centos/
  - гайд по установке docker-compose: https://docs.docker.com/compose/install/
- билд, запуск docker-контейнеров, накатывание миграций и сбор статики 
  (необходимо находиться в корне проекта, где распологается файл docker-compose.yaml)
```bash
$ docker-compose up -d --build
$ docker-compose exec storage python manage.py migrate --noinput
$ docker-compose exec storage python manage.py collectstatic
```
- после успешного запуска docker-контейнеров, приложение будет доступно по адресу: http://0.0.0.0:8080
  - если запуск происходит через удаленный сервер, то в качестве адреса указывается ip-адрес сервера
- для просмотра документации REST API, необходимо перейти по адресу: http://0.0.0.0:8080/api/docs
  - примечание: отправка списка объектов для их записи в базу через запрос: api/items/create, невозможна
    в стандартной спецификации OpenAPI при использовании swagger. Необходимо воспользоваться другим клиентом
    для отправки post-запроса, например, Postman.
- в случае неудачи при запуске docker-контейнеров, необходимо ввести следующую команду для просмотра логов:
```bash
$ docker-compose logs -f
```


## Тестирование c использования Docker
### Запуск с созданием базы
```bash
$ docker-compose exec storage pytest --create-db
```

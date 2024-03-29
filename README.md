## Описание:

Данный проект представляет API к сервису блогов Yatube, авторизация осуществляется посредством JWT токена





### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ln9var/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env (MacOS, Linux)
python -m venv env (Windows)
```

```
source env/bin/activate (MacOS, Linux)
source env/Scripts/activate (Windows)
```

```
python3 -m pip install --upgrade pip
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
python manage.py runserver
```

Документация:

Посмотреть перечень всех эндпоинтов можно после запуска проекта по адресу:

```
http://localhost:8000/redoc/
```

### Примеры запросов:

После запуска сервера необходимо зарегистрироваться и получить jwt-токен.

POST-запросом на адрес http://127.0.0.1:8000/api/v1/users/

```
{
  username: "{Yourlogin}"
  password: "{Yourpassword}"
}
```

зарегистрировать логин/пароль и
получить токен access тем же
POST-запросом на адрес 
http://127.0.0.1:8000/api/v1/jwt/create/

После будут доступны эндпойнты для анонимов, **авторизованных пользователей, _авторов контента_**
- http://127.0.0.1:8000/api/v1/      **GET**-запросы
- http://127.0.0.1:8000/api/v1/posts/ GET, **POST, _PUT, PATCH, DELETE_**
- http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ GET, **POST, _PUT, PATCH, DELETE_**
- http://127.0.0.1:8000/api/v1/groups/ GET
- http://127.0.0.1:8000/api/v1/follow/ **GET, POST**



## Авторы

[@igor-isht](https://github.com/igor-isht) - настройка эндпойнтов, JWT-аутентификация

[@yandex-praktikum](https://github.com/yandex-praktikum) - юнит-тесты

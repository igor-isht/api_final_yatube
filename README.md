## Описание:

Данный проект представляет API к сервису блогов Yatube




### Как запустить проект (Windows):

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ln9var/api_final_yatube.git
```

```
cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```


### Примеры запросов:

После запуска сервера необходимо зарегистрироваться и получить jwt-токен:

POST-запросом на адрес http://127.0.0.1:8000/users/ 

```
{
  username: "{Yourlogin}"
  password: "{Yourpassword}"
}
```

зарегистрировать логин/пароль и
получить токен access тем же
POST-запросом на адрес 
http://127.0.0.1:8000/jwt/create/

После будут доступны эндпойнты для анонимов, **авторизованных пользователей, _авторов контента_**
- http://127.0.0.1:8000/       **GET**-запросы
- http://127.0.0.1:8000/api/v1/posts/ GET, **POST, _PUT, PATCH, DELETE_**
- http://127.0.0.1:8000/api/v1/groups/ GET
- http://127.0.0.1:8000/api/v1/follow/ **GET, POST**


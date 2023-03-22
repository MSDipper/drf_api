<h2 alingn='center'></h2>

### Описание проекта:

    
## Разработка



##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

    venv\Scripts\activate.bat - Windows

    venv/bin/activate - Linux

##### 4) Устанавливить зависимости:

    pip install -r req.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate

##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить сервер

    python manage.py runserver
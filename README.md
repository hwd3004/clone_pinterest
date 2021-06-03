1. start

python version 3.9.5

vscode - using pylint, autopep8, pylance

pipenv install django

django-admin startproject clone_pinterest .

py.exe .\manage.py startapp accountapp

py.exe .\manage.py runserver

---

구글에서 django gitignore 검색하여서 .gitignore 작업

---

장고에서 환경변수 설정

pipenv install django-environ

https://django-environ.readthedocs.io/en/latest/

settings.py

```
import os
from pathlib import Path

import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
```

===

2. templates

settings.py

```
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
```

---

include, extends, block 구문을 이용한 뼈대 html 작업

===

3. static

정적 파일 관리하기
https://docs.djangoproject.com/ko/3.2/howto/static-files/

---

settings.py

```
...
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [BASE_DIR / 'static']
...
```

---

css 파일 적용

head.html

```
{% load static %}

<head>
...
    <link rel="stylesheet" href="{% static 'base.css' %}" />
</head>
```

===

4. Model, DB

py.exe .\manage.py makemigrations

py.exe .\manage.py migrate

===

5. CreateView

===

6. Login, Logout

===

7. django-bootstrap4

pipenv install django-bootstrap4

===

8. DetailView

===

9. UpdateView

===

10. DeleteView

===

11. Bug fix

===

12. Authentication

===

13. Decorator
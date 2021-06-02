1. start

python version 3.9.5

using pylint, autopep8, pylance

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
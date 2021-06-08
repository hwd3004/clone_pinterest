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

===

14. superuser, media

py.exe .\manage.py createsuperuser

pipenv install pillow

===

15. Profileapp, ModelForm

py.exe .\manage.py startapp profileapp

===

16. Profileapp

py.exe .\manage.py makemigrations

py.exe .\manage.py migrate

===

17. Profileapp

===

18. get_success_url, refactoring

===

19. MagicGrid

py.exe .\manage.py startapp articleapp

===

20. Articleapp

===

21. ListView, Pagination

===

22. Mixin, Commentapp

py.exe .\manage.py startapp commentapp

===

23. Commentapp

===

24. Responsive Layout

===

25. Projectapp

py.exe .\manage.py startapp projectapp

/clone_pinterest/settings.py

```
INSTALLED_APPS = [
    ...
    'projectapp',
]
```

/clone_pinterest/urls.py

```
urlpatterns = [
    ...
    path('projects/', include('projectapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

/projectapp/models.py

```
from django.db import models

class Project(models.Model):
    ...
```

/projectapp/forms.py

```
class ProjectCreationForm(ModelForm):
    ...
```

py.exe .\manage.py makemigrations

py.exe .\manage.py migrate

/projectapp/views.py

```
class ProjectCreateView(CreateView):
    ...

class ProjectDetailView(DetailView):
    ...

class ProjectListView(ListView):
    ...
```

/projectapp/templates/projectapp/create.html, detail.html, list.html
app 폴더의 templates 폴더 안에 또 app 폴더 만들어야함에 주의

/templates/snippets/card_project.html

/templates/snippets/pagination.html 수정
articleapp, projectapp 둘 다 사용 가능

===

26. MultipleObjectMixin, Projectapp

py.exe .\manage.py makemigrations

py.exe .\manage.py migrate

===

27. RedirectView, Subscribeapp

py.exe .\manage.py startapp subscribeapp


===

28. Field Lookup을 사용한 구독 페이지 구현

sql에서
```
select ... where project in (...);
```

이 명령어를 장고에서
```
Articles.objects.filter(project__in=projects)
```
__ 언더스코어 2개로 구현할 수 있다

Field Lookup 장고 Documentation 링크
https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups

===

29. WYSIWYG

Medium Editor

===

30. 정리 및 다듬기

===

31. 오라클 클라우드

강의에서는 vultr와 aws에 배포하였으나,

나는 오라클 클라우드에 배포하였음

pipenv를 사용하였으나, 강의와 똑같이
pip freeze > rerequirements.txt
로 rerequirements 생성

Gunicorn 설치

pipenv install gunicorn

pip freeze > rerequirements.txt
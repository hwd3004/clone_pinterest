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

---

오라클 클라우드 우분투에 도커 포테이너까지 설치가 된 후에 ip주소:9000 접속해서

dockerfile 작성
```
FROM python:3.9.5

WORKDIR /home/

RUN git clone -b 31.-오라클-클라우드 --single-branch https://github.com/hwd3004/clone_pinterest.git

WORKDIR /home/clone_pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=암호키입력" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "clone_pinterest.wsgi", "--bind", "0.0.0.0:8000"]
```

images
build a new image
이름은 django_test_image:3
dockerfile 업로드
build the image

networks
add network
nginx-django 생성, 다른건 건들일 필요 없이 생성만.

add container
이름은 django_container_gunicorn
advanced container settings에서
network 탭에서 network를 방금 만든 nginx-django로 해줌
deploy the container -->

오라클 우분투에서 root 계정 로그인을 열어줌
파일질라로 루트 계정으로 접속. 22번 포트

nginx.conf 파일 작성
```
worker_processes auto;

events {
    
}

http {
    server {
        listen 80;

        include mime.types;

        location /static/ {
            alias /data/static/;
        }

        location /media/ {
            alias /data/media/;
        }

        location / {
            proxy_pass http://django_container_gunicorn:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

home 디렉토리에서 django_course 디렉토리 만들어줌
nginx.conf 파일을 django_course 디렉토리 안에 넣어줌

도커 포테이너 메뉴에서 volumes 생성
이름은 static, media 2개 생성

```
컨테이너 생성

이름은 django_container_gunicorn
nginx.conf 파일에 있는 proxy_pass 값과 같아야함

image 입력칸에는 django_test_image:3
이전에 dockerfile 업로드하면서 만든 이미지 이름과 같아야함

advanced container settings에서 network는 nginx-django
volumes에는 컨테이너 입력칸에 /home/clone_pinterest/staticfiles/
dockerfile에 있는 WORKDIR /home/clone_pinterest/ 이 주소에서 staticfiles를 추가한 것임
volume 칸에는 static - local

map additional volume 클릭
컨테이너 입력칸에 /home/clone_pinterest/media/
volume 칸에는 media - local

deploy the container 클릭

```

컨테이너 생성
이름은 nginx, image는 nginx:latest
publish a new network port 클릭하여서 host와 container 모두 80으로 해줌
advanced container settings - network에서 nginx-django로 해줌
volumes에서는
/data/static/, static - local
/data/media/, media - local
/etc/nginx/nginx.conf, 우측의 volume 체크를 bind로 체크해줌, host 입력칸에 /home/django_course/nginx.conf 입력

deploy the container 클릭

컨테이너 생성
이름은 mariadb, image는 mariadb:10.5
advanced container settings의 env 탭에서
add environment variable 클릭
https://hub.docker.com/_/mariadb 참고
```
Starting a MariaDB instance is simple:

$ docker run -p 127.0.0.1:3306:3306  --name some-mariadb -e MARIADB_ROOT_PASSWORD=my-secret-pw -d mariadb:tag
```
부분에서 MARIADB_ROOT_PASSWORD 를 입력
value 입력칸에는 임시로 일단 password1234

---

개발 / 배포 설정 분리

clone_pinterest 폴더 밑에
settings 폴더를 만들고, 그 안에 __init__.py 파일 하나 생성
clone_pinterest 폴더 안에 있던 settings.py를 settings 폴더 안으로 옮겨줌
settings.py 이름을 base.py로 바꿔줌
deploy.py와 local.py 파일을 생성해줌
나머지는 git을 확인
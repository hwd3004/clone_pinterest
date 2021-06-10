"""clone_pinterest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from articleapp.views import ArticleListView
# from clone_pinterest import settings
from clone_pinterest.settings import base
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
# settings 의 import 가 다른 걸로 되어있어서 img 파일의 경로를 못 찾는 에러가 발생했었다

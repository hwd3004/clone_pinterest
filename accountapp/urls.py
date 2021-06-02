from accountapp.views import AccountCreateView, hello_world
from django.urls import path
from django.urls.conf import include

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create')
]

from django.urls import path
from . import views

app_name='App2'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('index', views.index,name='index'),
]
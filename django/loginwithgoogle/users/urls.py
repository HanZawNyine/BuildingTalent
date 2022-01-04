from django.urls import path,include
from . import views

app_name = "users"

urlpatterns = [
    path('', views.login),
    path('home', views.home, name="home"),
]

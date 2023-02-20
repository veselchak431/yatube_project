# ice_cream/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком сортов мороженого
    path('group/<slug:slug>', views.group_posts),
]
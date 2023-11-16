from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.main, name='list'),
    path('<int:id>', views.detail, name='detail'),
    path('create', views.create, name='create')
]

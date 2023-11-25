from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.main, name='list'),
    path('<int:pk>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('<int:pk>/stock', views.stock, name='stock')
]

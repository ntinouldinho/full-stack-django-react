from django.urls import path
from . import views

from django.contrib import admin
from django.urls import include, path
from .views import create_notification

urlpatterns = [
    path('notification/', create_notification),
]
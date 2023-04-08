from django.urls import path
from . import views

from .views import get_all_users, delete_user


urlpatterns = [
    path('users/', get_all_users, name='get_all_users'),
    path('user/<str:user_id>', delete_user, name='delete_user')
]

# urls.py

from django.urls import path
from .views import search,deleteSearch,history, store

urlpatterns = [
    path('search/', search, name='search-all'),
    path('search/<str:city>/', deleteSearch, name='search'),
    path('history/', history, name='history'),
    path('store/', store, name='store'),
]

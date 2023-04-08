# urls.py

from django.urls import path
from .views import search,deleteSearch,history

urlpatterns = [
    path('search/', search, name='search-all'),
    path('search/<str:city>/', deleteSearch, name='search'),
    path('history/', history, name='history'),

]

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notifications.urls')),
    path('', include('search.urls')),
    path('', include('users.urls')),
]
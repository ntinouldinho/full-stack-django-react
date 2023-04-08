from django.db import models

# Create your models here.

class Search(models.Model):
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
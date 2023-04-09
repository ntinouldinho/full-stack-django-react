from django.db import models
import json

# Create your models here.

class Search(models.Model):
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    

class WeatherData(models.Model):
    user_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def get_data(self):
        return json.loads(self.data)

    def set_data(self, data):
        self.data = json.dumps(data)
    
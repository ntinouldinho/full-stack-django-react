from django.db import models

class Notification(models.Model):
    email = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    send_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user} - {self.city} - {self.send_time}'

from django.db import models

class EmailSchedule(models.Model):
    user_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    send_time = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    current_time = models.DateTimeField(auto_now=True)


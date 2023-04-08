from django.db import models

class EmailSchedule(models.Model):
    user_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    current_time = models.DateTimeField(auto_now=True)


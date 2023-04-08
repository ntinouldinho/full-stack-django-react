from django.core.mail import send_mail
from django.conf import settings
from .celery import app
from notifications.models import EmailSchedule
from celery import shared_task

@app.task
def send_search_results_email(notification_id):
    notification = EmailSchedule.objects.get(id=notification_id)
    notification.status = True  
    notification.save()
    # subject = 'Weather Forecast'
    # message = 'You requested a weather forecase for:${city}'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['tinoathome@windowslive.com',]
    # send_mail( subject, message, email_from, recipient_list )
    return "SENT"

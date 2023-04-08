from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.serializers import serialize
import jwt
from auth0.authentication import GetToken
from auth0.management import Auth0
import os
import api.settings
import requests
# Create your views here.

    
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Notification

from datetime import datetime, timedelta
from api.tasks import send_search_results_email
from celery import current_app
from notifications.models import EmailSchedule
import pytz


@csrf_exempt
def create_notification(request):
    decoded_token = request.jwt_token

    if request.method == 'POST':
        
        data = json.loads(request.body.decode('utf-8'))
        city = data.get('city')
        email = data.get('email')
        date = data.get('date').replace('T',' ')[:-5]
        # london_tz = pytz.timezone('Europe/Athens')
        # london_dt = london_tz.localize(send_time)
        # send_time = london_dt.astimezone(pytz.UTC)
        
        notification = EmailSchedule(
                email=email,
                user_id=decoded_token['sub'],
                city=city,
        )
        try:
            notification.save()

            send_search_results_email.apply_async(args=[notification.id],eta=date)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
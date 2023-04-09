import datetime
from django.test import TestCase
from notifications.models import EmailSchedule
from rest_framework.test import APIClient
import time
# Create your tests here.


class NotificationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/notification/'
        self.headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJjbTFYVHVRVjd2cjVKXzhKT3E0RyJ9.eyJpc3MiOiJodHRwczovL2Rldi0yYnUycDdqYTVpb3M3MTAyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDJlN2Y3ZGM5YzZhMWQ3YmE4MWIwZTUiLCJhdWQiOlsiaHR0cHM6Ly9oZWxsby13b3JsZC5leGFtcGxlLmNvbSIsImh0dHBzOi8vZGV2LTJidTJwN2phNWlvczcxMDIudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4MTA2MDg1OSwiZXhwIjoxNjgxMTQ3MjU5LCJhenAiOiI4MnNGYUVxOFdQM2dURUd0ZGZWcm9VQm13Z3l0b1NYUiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnVzZXJzIl19.cGJKfScI1v_WYeF2_LyFRAASleX9MgA0-oz_BdRNT4AXJKb0J7-OLWtedEtjGMY-_vhw3w8VqnVg8Gai91s8f5x7D9aVjKx-BMJru0fPHmgBV-6cbaNeZesAMcUwCOFK7oXeSTL9Ch5TdOtn4TngP3v4cphH6oJPtRbVmxzNVHhn0-x3NALUOsnxMgtYLNPa23Xb5wFQu2dM1gErU1sJLJjfrirLfZuUTIIspHYqKnzuG5pFS8x2L-Gdf5DJJeYTohbcw5AyDQ6Ld6p5y48JUYTNPftCKf7BdaSSbqfww-mqaesxzdviRDBAcTlLwfs2XPFzR-B-P4jem1oIjyz96g'}
        
        now = datetime.datetime.utcnow()
        ten_seconds_later = now + datetime.timedelta(seconds=5)
        ten_seconds_later_str = ten_seconds_later.strftime('%Y-%m-%d %H:%M:%S')+'.....'

        self.data = {'city':"athens", 'date': ten_seconds_later_str, 'email' :"tinoathome@windowslive.com"}

        self.sub = "auth0|642e7f7dc9c6a1d7ba81b0e5"

        self.city = "athens"

    def test_api_response(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers.get('Authorization'))
        
        self.client.post(self.url, data=self.data, format='json')

        time.sleep(10)

        result = EmailSchedule.objects.filter(user_id=self.sub, city=self.city).first()
        
        self.assertEqual(result.status, False)
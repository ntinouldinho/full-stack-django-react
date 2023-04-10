import time
from django.test import TestCase
from rest_framework.test import APIClient

class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/history/'
        self.headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJjbTFYVHVRVjd2cjVKXzhKT3E0RyJ9.eyJpc3MiOiJodHRwczovL2Rldi0yYnUycDdqYTVpb3M3MTAyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDJlN2Y3ZGM5YzZhMWQ3YmE4MWIwZTUiLCJhdWQiOlsiaHR0cHM6Ly9oZWxsby13b3JsZC5leGFtcGxlLmNvbSIsImh0dHBzOi8vZGV2LTJidTJwN2phNWlvczcxMDIudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4MTA2MDg1OSwiZXhwIjoxNjgxMTQ3MjU5LCJhenAiOiI4MnNGYUVxOFdQM2dURUd0ZGZWcm9VQm13Z3l0b1NYUiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnVzZXJzIl19.cGJKfScI1v_WYeF2_LyFRAASleX9MgA0-oz_BdRNT4AXJKb0J7-OLWtedEtjGMY-_vhw3w8VqnVg8Gai91s8f5x7D9aVjKx-BMJru0fPHmgBV-6cbaNeZesAMcUwCOFK7oXeSTL9Ch5TdOtn4TngP3v4cphH6oJPtRbVmxzNVHhn0-x3NALUOsnxMgtYLNPa23Xb5wFQu2dM1gErU1sJLJjfrirLfZuUTIIspHYqKnzuG5pFS8x2L-Gdf5DJJeYTohbcw5AyDQ6Ld6p5y48JUYTNPftCKf7BdaSSbqfww-mqaesxzdviRDBAcTlLwfs2XPFzR-B-P4jem1oIjyz96g'}
    
    def test_api_response(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.headers.get('Authorization'))
        response = self.client.get(self.url, format='json', **self.headers)
        self.assertEqual(response.status_code, 200)


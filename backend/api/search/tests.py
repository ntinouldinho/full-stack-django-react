from django.test import TestCase

from .models import Search
from rest_framework.test import APIClient
# Create your tests here.

class SearchAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/search/'
        self.headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJjbTFYVHVRVjd2cjVKXzhKT3E0RyJ9.eyJpc3MiOiJodHRwczovL2Rldi0yYnUycDdqYTVpb3M3MTAyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDJlN2Y3ZGM5YzZhMWQ3YmE4MWIwZTUiLCJhdWQiOlsiaHR0cHM6Ly9oZWxsby13b3JsZC5leGFtcGxlLmNvbSIsImh0dHBzOi8vZGV2LTJidTJwN2phNWlvczcxMDIudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4MTA2MDg1OSwiZXhwIjoxNjgxMTQ3MjU5LCJhenAiOiI4MnNGYUVxOFdQM2dURUd0ZGZWcm9VQm13Z3l0b1NYUiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnVzZXJzIl19.cGJKfScI1v_WYeF2_LyFRAASleX9MgA0-oz_BdRNT4AXJKb0J7-OLWtedEtjGMY-_vhw3w8VqnVg8Gai91s8f5x7D9aVjKx-BMJru0fPHmgBV-6cbaNeZesAMcUwCOFK7oXeSTL9Ch5TdOtn4TngP3v4cphH6oJPtRbVmxzNVHhn0-x3NALUOsnxMgtYLNPa23Xb5wFQu2dM1gErU1sJLJjfrirLfZuUTIIspHYqKnzuG5pFS8x2L-Gdf5DJJeYTohbcw5AyDQ6Ld6p5y48JUYTNPftCKf7BdaSSbqfww-mqaesxzdviRDBAcTlLwfs2XPFzR-B-P4jem1oIjyz96g'}
        self.user_id = "auth0|642e7f7dc9c6a1d7ba81b0e5"
        self.data = {'city':'athens'}

    def test_post_city(self):
        
        self.client.credentials(HTTP_AUTHORIZATION=self.headers.get('Authorization'))
        
        response = self.client.post(self.url, data=self.data, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Search.objects.filter(user_id=self.user_id,city=self.data['city']).count(),1)

    # def test_get_city(self):
        
    #     self.client.credentials(HTTP_AUTHORIZATION=self.headers.get('Authorization'))
        
    #     response = self.client.get(self.url+'athens', content_type='application/json').json()
    #     print(response)
    #     self.assertEqual(response.status_code, 301)
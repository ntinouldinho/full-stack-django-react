from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
import jwt
from auth0.authentication import GetToken
from auth0.management import Auth0
import os
import api.settings
import requests
# Create your views here.


def get_all_users(request):
    
    users = []

    decoded_token = request.jwt_token

    if request.method == 'GET':

        if decoded_token.get("permissions"):
            if 'read:users' in decoded_token['permissions']:
                admin_token = api.settings.AUTH0_ADMIN_TOKEN
                
                headers = { 'authorization': "Bearer "+admin_token}


                res = requests.get("https://dev-2bu2p7ja5ios7102.us.auth0.com/api/v2/users", headers=headers).json()
                
                for user in res:
                    
                    last_ip = user['last_ip'] if 'last_ip' in user else ""
                    last_login = user['last_login'] if 'last_login' in user else ""

                    users.append({
                        'user_id': user['user_id'],
                        'email': user['email'],
                        'nickname':user['nickname'],
                        'last_ip': last_ip ,
                        'last_login':last_login,
                    })
                
                return JsonResponse(users, safe=False)
            
        else:
            return JsonResponse({'error': 'Invalid request method, permissions not set correctly'}, status=405)


@csrf_exempt
def delete_user(request,user_id):
    
    if request.method == 'DELETE':

        decoded_token = request.jwt_token

        if decoded_token.get("permissions"):
            if 'read:users' in decoded_token['permissions']:
                admin_token = api.settings.AUTH0_ADMIN_TOKEN

                headers = { 
                    'authorization': "Bearer "+admin_token,
                    'Content-Type': 'application/json'
                }

                url = f'https://dev-2bu2p7ja5ios7102.us.auth0.com/api/v2/users/{user_id}'

                # Send the DELETE request to the Auth0 Management API
                response = requests.delete(url, headers=headers)

                if response.status_code == 204:
                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'error', 'message': response.text})
        
        else:
            return JsonResponse({'error': 'Invalid request method, permissions not set correctly'}, status=405)



def check_permission(request):

    decoded_token = request.jwt_token

    if request.method == 'GET':

        if decoded_token.get("permissions"):
            if 'read:users' in decoded_token['permissions']:
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'incorrect permissions set'}, status=404)
        else:
                return JsonResponse({'status': 'error', 'message': 'incorrect permissions set'}, status=404)
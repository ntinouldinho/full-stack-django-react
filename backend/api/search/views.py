from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Search
from django.core.serializers import serialize
import jwt

# Create your views here.


@csrf_exempt
def search(request):

    decoded_token = request.jwt_token

    if request.method == 'POST':
        
        data = json.loads(request.body.decode('utf-8'))
        
        search = Search(user_id=decoded_token['sub'], city=data.get('city'), ip=request.META.get('REMOTE_ADDR'))
        try:
            search.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

        return JsonResponse({'success': True})

    elif request.method == 'GET':
        
        searches = Search.objects.filter(user_id=decoded_token['sub'],status=True)
        
        response_data = []
        for search in searches:
            response_data.append(search.city)
        

        return JsonResponse(list(set(response_data)),safe=False)

@csrf_exempt
def deleteSearch(request, city):

    decoded_token = request.jwt_token

    if request.method == 'DELETE':

        try:
            Search.objects.filter(user_id=decoded_token['sub'], city=city).update(status=False)
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False}, status=404)

@csrf_exempt   
def history(request):
    decoded_token = request.jwt_token
    
    if request.method == 'GET':
        
        searches = Search.objects.filter(user_id=decoded_token['sub'])
        
        data = serialize('json', searches)
            
        return JsonResponse(data, safe=False)
    
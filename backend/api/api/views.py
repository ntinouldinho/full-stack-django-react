import json
from authlib.integrations.django_oauth2 import ResourceProtector
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import validator
import http.client
import requests

# require_auth = ResourceProtector()
# validator = validator.Auth0JWTBearerTokenValidator(
#     'dev-2bu2p7ja5ios7102.us.auth0.com',
#     'https://dev-2bu2p7ja5ios7102.us.auth0.com/api/v2/'
# )
# require_auth.register_token_validator(validator)





import jwt
from django.http import JsonResponse

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get("Authorization").split(" ")[1]

        try:
            decoded_token = jwt.decode(
                token, options={"verify_signature": False}
            )
        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"message": "Invalid token"}, status=401)

        request.jwt_token = decoded_token

        response = self.get_response(request)

        return response

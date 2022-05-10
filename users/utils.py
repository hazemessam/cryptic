import jwt
from django.http import HttpRequest
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed
from core.settings import SECRET_KEY, JWT_LIFETIME_IN_DAYS


def generate_token(user_id, days=JWT_LIFETIME_IN_DAYS, **kwargs) -> str:
    payload: dict = {
        'user_id': user_id,
        'iat': timezone.now(),
        'exp': timezone.now() + timezone.timedelta(days=days)
    }
    
    for kwarg in kwargs:
        payload[kwarg] = kwargs[kwarg]
    
    token = jwt.encode(payload, SECRET_KEY)
    return token


def get_token(request: HttpRequest) -> str:
    try:
        token: str = request.headers.get('Authorization')
        token = token.split()[1]
        return token
    except:
        raise AuthenticationFailed()


def verify_token(token: str) -> dict:
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except:
        raise AuthenticationFailed()

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password, check_password
from django.core import exceptions as dj_exceptions
from django.http import HttpRequest
from rest_framework import exceptions as drf_exceptions
from users.models import User
from users.utils import generate_token, get_token, verify_token


class UserService:
    @staticmethod
    def add_user(
        name: str, username: str, password: str, **other_fields
    ) -> User:
        user: User = User(name=name, username=username)

        for field in other_fields:            
            setattr(user, field, other_fields)

        try: validate_password(password, user)
        except dj_exceptions.ValidationError as e:
            raise drf_exceptions.ValidationError(e.messages)
        user.password = make_password(password)

        user.save()
        return user


    @staticmethod
    def login(username: str, password: str) -> str:
        user: User = User.objects.filter(username=username).first()

        if not user: raise drf_exceptions.NotFound()

        if not check_password(password, user.password):
            raise drf_exceptions.AuthenticationFailed()

        token: str = generate_token(user.pk)
        return token


    @staticmethod
    def authenticate(request: HttpRequest) -> User:
        token: str = get_token(request)
        payload: dict = verify_token(token)

        user_id: int = payload.get('user_id')
        if not user_id:
            raise drf_exceptions.AuthenticationFailed()

        try: user: User = User.objects.get(pk=user_id)
        except dj_exceptions.ObjectDoesNotExist as e:
            raise drf_exceptions.NotFound(e)
        return user

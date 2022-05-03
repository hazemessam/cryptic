from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from users.models import User


class UserService:
    @classmethod
    def add_user(
        cls, name: str, username: str, password: str, **other_fields
    ) -> User:
        user: User = User(name=name, username=username)

        for field in other_fields:            
            setattr(user, field, other_fields)

        validate_password(password, user)
        user.password = make_password(password)
        
        user.save()
        return user

    @classmethod
    def get_user_by_id(cls, id: int) -> User:
        return User.objects.get(pk=id)

    @classmethod
    def get_user_by_username(cls, username: str) -> User:
        return User.objects.filter(username=username)

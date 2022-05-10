from rest_framework.serializers import ModelSerializer, CharField
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    password = CharField(write_only=True)

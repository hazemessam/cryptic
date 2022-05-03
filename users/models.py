from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = None
    name = models.CharField(max_length=50, null=False, blank=False)

from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True, null=False,
                                blank=False, validators=[UnicodeUsernameValidator()])
    password = models.CharField(max_length=50, null=False, blank=False)

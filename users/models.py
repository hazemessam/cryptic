from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    
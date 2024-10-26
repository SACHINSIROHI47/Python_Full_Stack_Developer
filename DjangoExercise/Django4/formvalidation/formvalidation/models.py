from django.db import models


class User(models.Model):
    # username field
    username = models.CharField(max_length=30, blank=False, null=False)
    # password field
    password = models.CharField(max_length=8, blank=False, null=False)
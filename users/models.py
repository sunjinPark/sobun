from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, unique=True, max_length=20)
    pwd = models.CharField(max_length=20)
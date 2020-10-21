from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime


class Account(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followers', blank=True)
    birth_date = models.DateField(blank=False, default=datetime.now())

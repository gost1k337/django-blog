from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, birth_date=None,
                    is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have an password')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.username = username
        user.set_password(password)
        user.birth_date = birth_date
        user.is_staff = is_staff
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user


class Account(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    followers = models.ManyToManyField('self', related_name='followers', blank=True)
    birth_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

from django.db import models
from django.contrib.auth.models import AbstractUser,  BaseUserManager
from employee_server.models.base import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email),
                          **kwargs)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, BaseModel):

    objects = UserManager()

    username = None

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

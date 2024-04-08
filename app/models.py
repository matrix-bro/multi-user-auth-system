from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username
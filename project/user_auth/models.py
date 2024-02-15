from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    phone = models.BigIntegerField()
    password = models.TextField()
    
    def save(self, *args, **kwargs) -> None:
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)
    
    def check_password(self, password=None):
        if password:
            if check_password(password, self.password):
                return True
        return False
    
    def __repr__(self):
        return f"{self.first_name}"
    def __str__(self):
        return self.first_name
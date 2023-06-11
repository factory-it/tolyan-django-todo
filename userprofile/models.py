from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

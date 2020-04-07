from django.db import models
from django.contrib.auth.models import AbstractUser

class BookUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="Возраст", null = True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

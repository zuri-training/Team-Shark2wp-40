from django.db import models
# from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import AbstractUser
from .user import CustomUserManager
from django.conf import settings
import uuid

CATEGORY_CHOICES = (
    ('S', 'School'),
    ('G', 'Guardian')
)


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email       = models.EmailField(max_length=120, unique=True) 
    is_school = models.BooleanField(default=False)
    is_guardian = models.BooleanField(default=False)
    school_name = models.CharField(max_length=250, blank=True)
    cac         = models.CharField(max_length=120, blank=True)
    student_name = models.CharField(max_length=120, default="", blank=True)
    # date_of_establishment = models.DateField( blank=True )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    object = CustomUserManager()

    class Meta:
        ordering = ["-email"]
        verbose_name = 'User'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




# Creating the guardian account model


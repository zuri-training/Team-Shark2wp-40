from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *



class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number", "school_name", "cac", 
         "password1", "password2"]
     
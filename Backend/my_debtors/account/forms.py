from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *



class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number",  "is_school", "is_guardian", "school_name", "student_name","cac", 
         "password1", "password2"]
     
from django.db import models
from django.urls import reverse


# Create your models here.

class SchoolAdmin(models.Model):
    name             = models.CharField(max_length=120) 
    school           = models.EmailField(max_length=120) 
    school_address   = models.CharField(max_length=250)
    email            = models.EmailField(max_length=120, default="")
    phone_no         = models.DecimalField(decimal_places=2, max_digits=15)
    admin_image      = models.ImageField(upload_to ='uploads/', blank=True) 
    def get_absolute_url(self):
        return reverse("school:add-schadmin", kwargs={"id": self.id})   


class Debtor(models.Model):
    debtor_name      = models.CharField(max_length=120) 
    ward_name        = models.CharField(max_length=120) 
    school           = models.CharField(max_length=120)
    debtor_class     = models.CharField(max_length=250)
    # date             = models.DateField(auto_now_add=True)
    amount_indebted  = models.DecimalField(decimal_places=2, max_digits=100000)
    phone_no         = models.DecimalField(decimal_places=0, max_digits=15)
    email            = models.EmailField(max_length=120, default="")
    debtor_image      = models.ImageField(upload_to ='uploads/', blank=True)  

    def get_absolute_url(self):
        return reverse("school:dashboard", kwargs={"id": self.id})  

class Message(models.Model):
    name             = models.CharField(max_length=120) 
    email            = models.EmailField(max_length=120, default="")
    message          = models.TextField(default='')
    image            = models.ImageField(upload_to ='uploads/', default='',blank=True) 
    document         = models.FileField(upload_to='uploads/', default='', blank=True)

    def get_absolute_url(self):
        return reverse("school:add-message", kwargs={"id": self.id}) 
from django.db import models


# Create your models here.

class SchoolAdmin(models.Model):
    name             = models.CharField(max_length=120) 
    school           = models.EmailField(max_length=120) 
    school_address   = models.CharField(max_length=250)
    date_of_est      = models.DateField(auto_now_add=True)
    CAC_no           = models.CharField(max_length=120)
    phone_no         = models.DecimalField(decimal_places=2, max_digits=15)
    admin_image      = models.ImageField(upload_to ='uploads/')   


class Debtor(models.Model):
    debtor_name      = models.CharField(max_length=120) 
    ward_name        = models.CharField(max_length=120) 
    school           = models.CharField(max_length=120)
    debtor_class     = models.CharField(max_length=250)
    date             = models.DateField(auto_now_add=True)
    amount_indebted  = models.DecimalField(decimal_places=2, max_digits=100000)
    phone_no         = models.DecimalField(decimal_places=2, max_digits=15)
    email            = models.EmailField(max_length=120)
    admin_image      = models.ImageField(upload_to ='uploads/')   

class Message(models.Model):
    name             = models.CharField(max_length=120) 
    email            = models.EmailField(max_length=120)
    message          = models.TextField()
    # image            = models.ImageField(upload_to ='uploads/') 


from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(SchoolAdmin)
admin.site.register(Debtor)
admin.site.register(Message)
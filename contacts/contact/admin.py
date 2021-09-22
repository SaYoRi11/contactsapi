from django.contrib import admin
from .models import Contact, Email, Phone_no

admin.site.register([Contact, Email, Phone_no])

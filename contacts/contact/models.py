from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    nick_name = models.CharField(max_length = 20)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('first_name',)

class Email(models.Model):
    email = models.EmailField(max_length=100)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.email

class Phone_no(models.Model):
    label_choices = (
        ('Home', 'Home'),
        ('Office', 'Office'),
        ('Work', 'Work'),
        ('Mobile', 'Mobile')
    )

    country_code = models.CharField(max_length=10, default='+1')
    phone_number = models.CharField(max_length=20)
    label = models.CharField(max_length=20, choices=label_choices, default='Home')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_nos')
    
    def __str__(self):
        return self.phone_number
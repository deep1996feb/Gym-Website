from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField( max_length=100)
    age = models.IntegerField()
    mobile = models.IntegerField( )
    address = models.CharField( max_length=100)

   
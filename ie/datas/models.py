from django.db import models

from datetime import date
from django.contrib.auth.models import  User
import datetime






class select(models.Model):
    sele = models.CharField(max_length= 20)

class product(models.Model):
    product_name = models.CharField(max_length=200,default =0)
    product_details = models.TextField(default =0)
    price = models.IntegerField(default =0)
    active = models.IntegerField(default='1')


class order(models.Model):

    name = models.CharField(max_length=200,default =0)
    phone = models.CharField(max_length=20,default =0)
    address = models.TextField(default =0)

    product_id = models.ForeignKey(product,on_delete=models.CASCADE,default= 0)
    payment_option = models.CharField(max_length=50,default =0)

    quantity = models.IntegerField(default= 0)










# Create your models here.

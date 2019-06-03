from django.db import models
from datetime import date
from django.contrib.auth.models import  User

#lines = [('EP-1','EP-1'),('EP-2A','EP-2A'),('EP-2B','EP-2B'),('EP-3A','EP-3A'),('EP-3B','EP-3B'),('EP-4','EP-4'),('EP-5A','EP-5A'),('EP-5B','EP-5B'),('EP-6','EP-6'),('EP-7A','EP-7A'),('EP-7B','EP-7B'),('EP-8A','EP-8A'),('EP-8B','EP-8B'),('EP-9','EP-9'),('EP-10','EP-10'),('EP-11A','EP-11A'),('EP-11B','EP-11B'),('EP-12','EP-12'),('EP-13','EP-13'),('EP-14A','EP-14A'),('EP-14B','EP-14B'),('EP-15A','EP-15A'),('EP-15B','EP-15B'),('EP-16A','EP-16A'),('EP-16B','EP-16B'),('EP-17','EP-17'),('EP-18','EP-18'),('EP-19','EP-19'),('EP-20','EP-20'),('EP-21','EP-21'),('EP-22','EP-22')]



class quality(models.Model):
    name = models.CharField(max_length = 20,default = 0)
    factoryname = models.CharField(max_length =20,default=0)
    category = models.CharField(max_length = 30,default=0)
    sub_category = models.CharField(max_length = 40,default=0)
    department = models.CharField(max_length = 40,default=0)
    section = models.CharField(max_length = 40,default=0)
    item_no = models.IntegerField(default=0)
    style_name = models.CharField(max_length = 40,default=0)
    style_number = models.IntegerField(default=0)
    #user_name = models.CharField(max_length =40,default=0)
    #user_id = models.CharField(max_length = 40,default=0)
    date = models.DateField(("Date"), default=date.today)
    EP_1 = models.FloatField(max_length=10,default=0 )
    EP_2 = models.FloatField(max_length=10, default=0)
    EP_3 = models.FloatField(max_length=10,default=0 )
    EP_4 = models.FloatField(max_length=10,default=0 )
    EP_5 = models.FloatField(max_length=10, default=0)
    EP_6 = models.FloatField(max_length=10, default=0)
    EP_7 = models.FloatField(max_length=10, default=0)
    EP_8 = models.FloatField(max_length=10, default=0)
    EP_9 = models.FloatField(max_length=10, default=0)
    EP_10 = models.FloatField(max_length=10, default=0)
    EP_11 = models.FloatField(max_length=10, default=0)
    EP_12 = models.FloatField(max_length=10, default=0)
    EP_13 = models.FloatField(max_length=10, default=0)
    EP_14 = models.FloatField(max_length=10, default=0)
    EP_15 = models.FloatField(max_length=10, default=0)
    EP_16 = models.FloatField(max_length=10, default=0)
    EP_17 = models.FloatField(max_length=10, default=0)
    EP_18 = models.FloatField(max_length=10, default=0)
    EP_19 = models.FloatField(max_length=10, default=0)
    EP_20 = models.FloatField(max_length=10, default=0)
    EP_21 = models.FloatField(max_length=10, default=0)
    EP_22  = models.FloatField(max_length=10, default=0)
    EP_23 = models.FloatField(max_length=10, default=0)
    EP_24 = models.FloatField(max_length=10, default=0)





class total(models.Model):
    total_checked = models.IntegerField(max_length=None,default=0)
    total_defects = models.IntegerField(max_length=None,default=0)
    total_passed = models.IntegerField(max_length=None,default=0)
# Create your models here.


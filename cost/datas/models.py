from django.db import models
from django.db import models
from datetime import date
from django.contrib.auth.models import  User

#lines = [('EP-1','EP-1'),('EP-2A','EP-2A'),('EP-2B','EP-2B'),('EP-3A','EP-3A'),('EP-3B','EP-3B'),('EP-4','EP-4'),('EP-5A','EP-5A'),('EP-5B','EP-5B'),('EP-6','EP-6'),('EP-7A','EP-7A'),('EP-7B','EP-7B'),('EP-8A','EP-8A'),('EP-8B','EP-8B'),('EP-9','EP-9'),('EP-10','EP-10'),('EP-11A','EP-11A'),('EP-11B','EP-11B'),('EP-12','EP-12'),('EP-13','EP-13'),('EP-14A','EP-14A'),('EP-14B','EP-14B'),('EP-15A','EP-15A'),('EP-15B','EP-15B'),('EP-16A','EP-16A'),('EP-16B','EP-16B'),('EP-17','EP-17'),('EP-18','EP-18'),('EP-19','EP-19'),('EP-20','EP-20'),('EP-21','EP-21'),('EP-22','EP-22')]



class cost(models.Model):
    line = models.CharField(max_length = 20,default =0)
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

    month = models.CharField(max_length= 20,default =0)
    year = models.CharField(max_length= 20,default =0)
    EP_1_manpower = models.FloatField(max_length=10,default=0 )
    EP_1_operator = models.FloatField(max_length=10, default=0)
    EP_1_minutes = models.FloatField(max_length=10, default=0)
    EP_1_cost = models.FloatField(max_length=10, default=0)

    EP_2_manpower = models.FloatField(max_length=10, default=0)
    EP_2_operator = models.FloatField(max_length=10, default=0)
    EP_2_minutes = models.FloatField(max_length=10, default=0)
    EP_2_cost = models.FloatField(max_length=10, default=0)
    EP_3_manpower = models.FloatField(max_length=10,default=0 )
    EP_3_operator = models.FloatField(max_length=10, default=0)
    EP_3_minutes = models.FloatField(max_length=10, default=0)
    EP_3_cost = models.FloatField(max_length=10, default=0)
    EP_4_manpower = models.FloatField(max_length=10,default=0 )
    EP_4_operator = models.FloatField(max_length=10, default=0)
    EP_4_minutes = models.FloatField(max_length=10, default=0)
    EP_4_cost = models.FloatField(max_length=10, default=0)
    EP_5_manpower = models.FloatField(max_length=10, default=0)
    EP_5_operator = models.FloatField(max_length=10, default=0)
    EP_5_minutes = models.FloatField(max_length=10, default=0)
    EP_5_cost = models.FloatField(max_length=10, default=0)
    EP_6_manpower = models.FloatField(max_length=10, default=0)
    EP_6_operator = models.FloatField(max_length=10, default=0)
    EP_6_minutes = models.FloatField(max_length=10, default=0)
    EP_6_cost = models.FloatField(max_length=10, default=0)
    EP_7_manpower = models.FloatField(max_length=10, default=0)
    EP_7_operator = models.FloatField(max_length=10, default=0)
    EP_7_minutes = models.FloatField(max_length=10, default=0)
    EP_7_cost = models.FloatField(max_length=10, default=0)
    EP_8_manpower = models.FloatField(max_length=10, default=0)
    EP_8_opeartor = models.FloatField(max_length=10, default=0)
    EP_8_minute = models.FloatField(max_length=10, default=0)
    EP_8_cost = models.FloatField(max_length=10, default=0)
    EP_9_manpower = models.FloatField(max_length=10, default=0)
    EP_9_operator = models.FloatField(max_length=10, default=0)
    EP_9_minutes = models.FloatField(max_length=10, default=0)
    EP_9_cost = models.FloatField(max_length=10, default=0)
    EP_10_manpower = models.FloatField(max_length=10, default=0)
    EP_10_opeartor = models.FloatField(max_length=10, default=0)
    EP_10_minutes = models.FloatField(max_length=10, default=0)
    EP_10_cost = models.FloatField(max_length=10, default=0)









class minu(models.Model):
    day = models.CharField(max_length= 20,default =0)

    month = models.CharField(max_length= 20,default =0)
    year = models.CharField(max_length= 20,default =0)
    minutes = models.IntegerField(max_length=None,default=0)
    line = models.CharField(max_length=20,default=0)

# Create your models here.
#class expences(models.Model):
class expenses(models.Model):
    factoryname = models.CharField(max_length = 20)
    month = models.CharField(max_length = 20)
    year = models.CharField(max_length= 20)
    wages = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    carrying = models.IntegerField(default=0)
    earn = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    epf = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    supplies = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    fuel = models.IntegerField(default=0)
    cf = models.IntegerField(default=0)
    frieght = models.IntegerField(default=0)
    insurence = models.IntegerField(default=0)
    labour = models.IntegerField(default=0)
    land = models.IntegerField(default=0)
    medical = models.IntegerField(default=0)
    miscellaneous = models.IntegerField(default=0)
    repair = models.IntegerField(default=0)
    tolls = models.IntegerField(default=0)
    transportation = models.IntegerField(default=0)
    total = models.IntegerField(default =0)
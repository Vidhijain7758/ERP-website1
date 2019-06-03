from django.db import models
from django.db import models
from datetime import date
from django.contrib.auth.models import  User

#lines = [('EP-1','EP-1'),('EP-2A','EP-2A'),('EP-2B','EP-2B'),('EP-3A','EP-3A'),('EP-3B','EP-3B'),('EP-4','EP-4'),('EP-5A','EP-5A'),('EP-5B','EP-5B'),('EP-6','EP-6'),('EP-7A','EP-7A'),('EP-7B','EP-7B'),('EP-8A','EP-8A'),('EP-8B','EP-8B'),('EP-9','EP-9'),('EP-10','EP-10'),('EP-11A','EP-11A'),('EP-11B','EP-11B'),('EP-12','EP-12'),('EP-13','EP-13'),('EP-14A','EP-14A'),('EP-14B','EP-14B'),('EP-15A','EP-15A'),('EP-15B','EP-15B'),('EP-16A','EP-16A'),('EP-16B','EP-16B'),('EP-17','EP-17'),('EP-18','EP-18'),('EP-19','EP-19'),('EP-20','EP-20'),('EP-21','EP-21'),('EP-22','EP-22')]



class ie(models.Model):
    month = models.CharField(max_length = 20, default =0)
    year = models.IntegerField(default =0 )


    mmr_budgeted = models.FloatField(default =0)
    mmr_actual = models.FloatField(default =0)
    no_lines = models.FloatField(default =0)
    machines_line = models.IntegerField(default =0)
    machine_oper = models.FloatField(default =0)

    sampling_bud = models.IntegerField(default =0)
    sampling_actual = models.IntegerField(default =0)
    pattern_bud = models.IntegerField(default =0)
    pattern_actual = models.IntegerField(default =0)
    fabric_bud = models.IntegerField(default =0)
    fabric_actual = models.IntegerField(default =0)
    trim_bud = models.IntegerField(default =0)
    trim_actual = models.IntegerField(default =0)
    cutting_bud = models.IntegerField(default =0)
    cutting_actual = models.IntegerField(default =0)
    sewing_bud = models.IntegerField(default =0)
    sewing_actual = models.IntegerField(default =0)
    ware_bud = models.IntegerField(default =0)
    ware_actual = models.IntegerField(default =0)
    planning_bud = models.IntegerField(default =0)
    planning_actual = models.IntegerField(default =0)
    ie_bud = models.IntegerField(default =0)
    ie_actual = models.IntegerField(default =0)
    maintainance_bud = models.IntegerField(default =0)
    maintainance_actual = models.IntegerField(default =0)














# Create your models here.

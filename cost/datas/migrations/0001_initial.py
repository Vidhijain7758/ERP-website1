# Generated by Django 2.0.6 on 2018-07-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(default=0, max_length=20)),
                ('name', models.CharField(default=0, max_length=20)),
                ('factoryname', models.CharField(default=0, max_length=20)),
                ('category', models.CharField(default=0, max_length=30)),
                ('sub_category', models.CharField(default=0, max_length=40)),
                ('department', models.CharField(default=0, max_length=40)),
                ('section', models.CharField(default=0, max_length=40)),
                ('item_no', models.IntegerField(default=0)),
                ('style_name', models.CharField(default=0, max_length=40)),
                ('style_number', models.IntegerField(default=0)),
                ('month', models.CharField(default=0, max_length=20)),
                ('year', models.CharField(default=0, max_length=20)),
                ('EP_1_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_1_operator', models.FloatField(default=0, max_length=10)),
                ('EP_1_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_1_cost', models.FloatField(default=0, max_length=10)),
                ('EP_2_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_2_operator', models.FloatField(default=0, max_length=10)),
                ('EP_2_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_2_cost', models.FloatField(default=0, max_length=10)),
                ('EP_3_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_3_operator', models.FloatField(default=0, max_length=10)),
                ('EP_3_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_3_cost', models.FloatField(default=0, max_length=10)),
                ('EP_4_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_4_operator', models.FloatField(default=0, max_length=10)),
                ('EP_4_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_4_cost', models.FloatField(default=0, max_length=10)),
                ('EP_5_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_5_operator', models.FloatField(default=0, max_length=10)),
                ('EP_5_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_5_cost', models.FloatField(default=0, max_length=10)),
                ('EP_6_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_6_operator', models.FloatField(default=0, max_length=10)),
                ('EP_6_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_6_cost', models.FloatField(default=0, max_length=10)),
                ('EP_7_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_7_operator', models.FloatField(default=0, max_length=10)),
                ('EP_7_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_7_cost', models.FloatField(default=0, max_length=10)),
                ('EP_8_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_8_opeartor', models.FloatField(default=0, max_length=10)),
                ('EP_8_minute', models.FloatField(default=0, max_length=10)),
                ('EP_8_cost', models.FloatField(default=0, max_length=10)),
                ('EP_9_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_9_operator', models.FloatField(default=0, max_length=10)),
                ('EP_9_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_9_cost', models.FloatField(default=0, max_length=10)),
                ('EP_10_manpower', models.FloatField(default=0, max_length=10)),
                ('EP_10_opeartor', models.FloatField(default=0, max_length=10)),
                ('EP_10_minutes', models.FloatField(default=0, max_length=10)),
                ('EP_10_cost', models.FloatField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factoryname', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('wages', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('carrying', models.IntegerField(default=0)),
                ('earn', models.IntegerField(default=0)),
                ('electricity', models.IntegerField(default=0)),
                ('epf', models.IntegerField(default=0)),
                ('rent', models.IntegerField(default=0)),
                ('supplies', models.IntegerField(default=0)),
                ('food', models.IntegerField(default=0)),
                ('fuel', models.IntegerField(default=0)),
                ('cf', models.IntegerField(default=0)),
                ('frieght', models.IntegerField(default=0)),
                ('insurence', models.IntegerField(default=0)),
                ('labour', models.IntegerField(default=0)),
                ('land', models.IntegerField(default=0)),
                ('medical', models.IntegerField(default=0)),
                ('miscellaneous', models.IntegerField(default=0)),
                ('repair', models.IntegerField(default=0)),
                ('tolls', models.IntegerField(default=0)),
                ('transportation', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='minu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default=0, max_length=20)),
                ('month', models.DateField(default=0, max_length=20)),
                ('year', models.DateField(default=0, max_length=20)),
                ('minutes', models.IntegerField(default=0)),
                ('line', models.CharField(default=0, max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0012_auto_20180620_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsconfig',
            name='gs_id',
            field=models.IntegerField(verbose_name='游戏服id'),
        ),
    ]

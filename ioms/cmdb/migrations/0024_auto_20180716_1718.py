# Generated by Django 2.0.6 on 2018-07-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0023_auto_20180716_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gsconfig',
            name='R',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='big_r',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='level',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='powerest_alliance_m',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='powerest_m',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='pvp',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='revenue',
        ),
        migrations.AlterField(
            model_name='gsconfig',
            name='power_m',
            field=models.FloatField(null=True, verbose_name='实力'),
        ),
    ]

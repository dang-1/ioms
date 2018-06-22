# Generated by Django 2.0.4 on 2018-06-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0015_auto_20180620_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbconfig',
            name='open_time',
            field=models.CharField(blank=True, max_length=42, verbose_name='database open time'),
        ),
        migrations.AlterField(
            model_name='dbconfig',
            name='status',
            field=models.CharField(max_length=42, verbose_name='database status, online of offline'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-05 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20180605_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbconfig',
            name='db_user',
        ),
    ]

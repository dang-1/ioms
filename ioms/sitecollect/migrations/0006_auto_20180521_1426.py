# Generated by Django 2.0.4 on 2018-05-21 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitecollect', '0005_auto_20180428_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitecollectmodel',
            options={'ordering': ['id', 'typeid']},
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostmanage', '0002_auto_20180323_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
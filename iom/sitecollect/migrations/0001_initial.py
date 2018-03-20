# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=60)),
                ('siteurl', models.CharField(max_length=60)),
                ('typeid', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=60)),
                ('typeid', models.CharField(max_length=60)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50)),
                ('hostip', models.CharField(max_length=50)),
                ('gs_zone', models.CharField(max_length=50)),
                ('gs_alias', models.CharField(max_length=50)),
                ('gs_accelerate_port', models.CharField(max_length=50)),
                ('gs_dir', models.CharField(max_length=50)),
                ('gs_name', models.CharField(max_length=50)),
                ('gs_db_outer_ip', models.CharField(max_length=50)),
                ('gs_db_inner_ip', models.CharField(max_length=50)),
                ('gs_status', models.CharField(max_length=50)),
                ('gs_open_time', models.CharField(max_length=50)),
                ('gs_branch', models.CharField(max_length=50)),
                ('gs_branch_commit_id', models.CharField(max_length=50)),
                ('gs_merged', models.CharField(max_length=50)),
                ('gs_merged_time', models.CharField(max_length=50)),
                ('gs_merged_to', models.CharField(max_length=50)),
            ],
        ),
    ]

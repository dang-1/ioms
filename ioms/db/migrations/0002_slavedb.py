# Generated by Django 2.0.4 on 2018-06-27 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostmanage', '0002_auto_20180524_1115'),
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlaveDb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=48, verbose_name='别名')),
                ('db_port', models.CharField(default=3306, max_length=42, verbose_name='database port')),
                ('status', models.CharField(max_length=42, verbose_name='database status, online of offline')),
                ('open_time', models.CharField(blank=True, max_length=42, verbose_name='database open time')),
                ('db_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slave_info', to='db.MasterDb', verbose_name='从库')),
                ('host_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slave_host_info', to='hostmanage.Host', verbose_name="host ip's id")),
            ],
            options={
                'ordering': ['id', 'alias'],
            },
        ),
    ]

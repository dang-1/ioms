# Generated by Django 2.0.6 on 2018-08-16 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20180815_1645'),
        ('hostmanage', '0002_auto_20180814_1706'),
        ('cmdb', '0002_auto_20180719_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='GwConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gs_db', models.CharField(blank=True, max_length=42, null=True, verbose_name='database name')),
                ('gs_db_ip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gw_db', to='db.MasterDb', verbose_name='main db')),
                ('gs_ip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gw_ip_info', to='hostmanage.Host', verbose_name="host ip's id")),
            ],
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='dau',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='power_alliance_m',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='power_m',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='udid',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='users',
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='gs_language',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='语言'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0017_gsconfig_gs_db_slave_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbconfig',
            name='alias',
            field=models.CharField(blank=True, max_length=48, verbose_name='别名'),
        ),
    ]
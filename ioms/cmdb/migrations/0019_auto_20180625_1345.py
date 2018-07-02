# Generated by Django 2.0.4 on 2018-06-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0018_dbconfig_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbconfig',
            name='db_slave_port',
            field=models.CharField(default=3306, max_length=42, verbose_name='database slave port'),
        ),
        migrations.AlterField(
            model_name='dbconfig',
            name='db_port',
            field=models.CharField(default=3306, max_length=42, verbose_name='database port'),
        ),
    ]
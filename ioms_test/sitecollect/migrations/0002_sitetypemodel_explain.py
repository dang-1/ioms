# Generated by Django 2.0.6 on 2018-08-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecollect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitetypemodel',
            name='explain',
            field=models.CharField(max_length=128, null=True, verbose_name='说明'),
        ),
    ]

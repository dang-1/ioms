# Generated by Django 2.0.6 on 2018-07-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0025_auto_20180716_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsconfig',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='gs_tag', to='cmdb.Tag', verbose_name='标签字段'),
        ),
    ]
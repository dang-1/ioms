# Generated by Django 2.0.6 on 2018-07-19 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gsconfig',
            name='tag',
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gs_tag', to='cmdb.Tag', verbose_name='标签字段'),
        ),
    ]

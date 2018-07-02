# Generated by Django 2.0.4 on 2018-06-20 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostmanage', '0002_auto_20180524_1115'),
        ('cmdb', '0009_auto_20180620_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gsconfig',
            old_name='gs_slave_ip',
            new_name='gs_db_slave_ip',
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='gs_db_ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='db_ip', to='hostmanage.Host', verbose_name="db ip's id"),
        ),
        migrations.AlterField(
            model_name='gsconfig',
            name='gs_ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gs_ip_info', to='hostmanage.Host', verbose_name="host ip's id"),
        ),
    ]
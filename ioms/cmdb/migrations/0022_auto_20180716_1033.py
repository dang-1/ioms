# Generated by Django 2.0.6 on 2018-07-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0021_gsconfig_gs_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbconfig',
            name='master_ip',
        ),
        migrations.RemoveField(
            model_name='dbconfig',
            name='slave_ip',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='gs_db_info',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='gs_db_ip',
        ),
        migrations.RemoveField(
            model_name='gsconfig',
            name='gs_db_slave_ip',
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='R',
            field=models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='big_r',
            field=models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='dau',
            field=models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='level',
            field=models.CharField(max_length=128, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='power_alliance_m',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='power_m',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='powerest_alliance_m',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='powerest_m',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='pvp',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='revenue',
            field=models.FloatField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='udid',
            field=models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='update_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='gsconfig',
            name='users',
            field=models.IntegerField(null=True, verbose_name='用户数量'),
        ),
        migrations.DeleteModel(
            name='DbConfig',
        ),
    ]
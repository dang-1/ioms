# Generated by Django 2.0 on 2018-04-26 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostmanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gs_zone', models.CharField(max_length=50, verbose_name='区域')),
                ('gs_id', models.CharField(max_length=50, verbose_name='游戏服id')),
                ('gs_alias', models.CharField(max_length=50, verbose_name='唯一标识符')),
                ('gs_accelerate_port', models.CharField(max_length=50, verbose_name='加速端口')),
                ('gs_dir', models.CharField(max_length=50, verbose_name='游戏服目录')),
                ('gs_name', models.CharField(max_length=50, verbose_name='游戏服名字')),
                ('gs_open_time', models.CharField(max_length=50, verbose_name='开服时间')),
                ('gs_branch', models.CharField(max_length=50, verbose_name='分支名')),
                ('gs_branch_commit_id', models.CharField(max_length=50, verbose_name='分支的commit id')),
                ('gs_merged', models.CharField(max_length=50, verbose_name='是否合服')),
                ('gs_merged_time', models.CharField(max_length=50, verbose_name='合服时间')),
                ('gs_merged_to_id', models.CharField(max_length=50, verbose_name='合入id')),
                ('gs_ip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostmanage.Host', verbose_name="host ip's id")),
            ],
            options={
                'ordering': ['gs_zone', 'gs_id'],
            },
        ),
        migrations.CreateModel(
            name='DbConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('db_user', models.CharField(max_length=42, verbose_name='database user')),
                ('db_port', models.CharField(default='3306', max_length=42, verbose_name='database port')),
                ('db_name', models.CharField(max_length=42, verbose_name='database name')),
                ('status', models.CharField(max_length=42, verbose_name='database status')),
                ('host_ip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostmanage.Host', verbose_name="host ip's id")),
            ],
        ),
        migrations.CreateModel(
            name='GsStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=48, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_name', models.CharField(max_length=48, unique=True)),
            ],
            options={
                'ordering': ['zone_name'],
            },
        ),
        migrations.AddField(
            model_name='configmanage',
            name='gs_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.GsStatus', verbose_name='gs status id'),
        ),
    ]
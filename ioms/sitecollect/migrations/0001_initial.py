# Generated by Django 2.0.6 on 2018-07-18 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteCollectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(default='test', max_length=60, unique=True, verbose_name='链接名称')),
                ('siteurl', models.CharField(default='test', max_length=60, unique=True, verbose_name='链接地址')),
            ],
            options={
                'ordering': ['id', 'typeid'],
            },
        ),
        migrations.CreateModel(
            name='SiteTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('site_type_name', models.CharField(max_length=60, unique=True, verbose_name='网址类型')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='sitecollectmodel',
            name='typeid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sitecollect.SiteTypeModel', verbose_name='名称'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-07-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostmanage', '0003_auto_20180713_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostrole',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='hostrole',
            name='explain',
            field=models.CharField(max_length=128, null=True, verbose_name='说明'),
        ),
    ]
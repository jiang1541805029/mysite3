# Generated by Django 3.1.3 on 2020-11-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201111_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jingdian',
            name='open_time',
            field=models.CharField(max_length=100),
        ),
    ]

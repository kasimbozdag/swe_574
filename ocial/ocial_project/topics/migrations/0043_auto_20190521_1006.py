# Generated by Django 2.2 on 2019-05-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0042_auto_20190521_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='completeRate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='completeRate',
            field=models.FloatField(default=0),
        ),
    ]

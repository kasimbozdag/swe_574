# Generated by Django 2.2 on 2019-04-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_auto_20190414_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='label',
            field=models.ManyToManyField(to='topics.Label'),
        ),
    ]
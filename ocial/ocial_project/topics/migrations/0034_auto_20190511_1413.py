# Generated by Django 2.2 on 2019-05-11 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0033_auto_20190511_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glossary',
            old_name='label',
            new_name='name',
        ),
    ]
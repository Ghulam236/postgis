# Generated by Django 4.1.1 on 2022-10-03 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangopostgis', '0002_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='nl_name_1',
        ),
        migrations.RemoveField(
            model_name='country',
            name='varname_1',
        ),
    ]

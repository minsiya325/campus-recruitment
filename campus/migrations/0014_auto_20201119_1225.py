# Generated by Django 3.0.8 on 2020-11-19 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0013_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='type',
        ),
        migrations.RemoveField(
            model_name='stud_reg',
            name='type',
        ),
    ]

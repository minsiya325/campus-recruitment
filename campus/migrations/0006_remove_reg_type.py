# Generated by Django 3.0.8 on 2020-10-28 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0005_remove_stud_reg_college'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='type',
        ),
    ]

# Generated by Django 3.1.1 on 2021-01-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0039_auto_20210109_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud_reg',
            name='dob',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stud_reg',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
# Generated by Django 3.0.8 on 2020-12-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0028_auto_20201130_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_desc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
# Generated by Django 3.0.8 on 2020-11-28 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0024_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campus.Course'),
        ),
    ]
# Generated by Django 3.0.8 on 2020-12-13 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0033_auto_20201204_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatstudent',
            old_name='member',
            new_name='status',
        ),
    ]

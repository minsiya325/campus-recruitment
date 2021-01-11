# Generated by Django 3.0.8 on 2020-12-04 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0032_chatstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatstudent',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campus.Stud_Reg'),
        ),
        migrations.AlterField(
            model_name='placedstudent',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campus.Stud_Reg'),
        ),
    ]
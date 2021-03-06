# Generated by Django 3.0.8 on 2020-11-25 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0019_remove_stud_reg_college_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud_reg',
            name='course',
        ),
        migrations.RemoveField(
            model_name='stud_reg',
            name='sem',
        ),
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_p', models.CharField(max_length=100)),
                ('twe_p', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('ug', models.CharField(max_length=100)),
                ('pg', models.CharField(max_length=100)),
                ('cv', models.ImageField(null=True, upload_to='images/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.Stud_Reg')),
            ],
        ),
    ]

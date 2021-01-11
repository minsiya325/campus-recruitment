from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=True)
    joindate = models.CharField(max_length=100,null=True)


class Course(models.Model):
    name = models.CharField(max_length=100,null=True)
    graduate = models.CharField(max_length=100)


class Stud_Reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    saddress = models.CharField(max_length=100)
    scontact = models.CharField(max_length=100)
    adno = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)

    image = models.ImageField(upload_to='images/', null=True)

class Academic(models.Model):
    student = models.ForeignKey(Stud_Reg,on_delete=models.CASCADE)
    ten_p = models.CharField(max_length=100)
    twe_p = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    ug = models.CharField(max_length=100,null=True)
    batch = models.CharField(max_length=100,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    cv = models.ImageField(upload_to='images/', null=True)


class Placement(models.Model):
    p_name = models.CharField(max_length=100)
    p_address = models.CharField(max_length=100)
    p_contact = models.CharField(max_length=100)

    p_date = models.CharField(max_length=100,null=True)
    p_time = models.CharField(max_length=100,null=True)
    brochure = models.ImageField(upload_to='images/', null=True)

class Job(models.Model):
    drive = models.ForeignKey(Placement,on_delete=models.CASCADE)
    company = models.ForeignKey(Reg,on_delete=models.CASCADE,null=True)
    p_course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    p_name = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    no_vacan = models.CharField(max_length=100,null=True)
    salary = models.CharField(max_length=100,null=True)
    p_per = models.CharField(max_length=100,null=True)
    p_sem = models.CharField(max_length=100,null=True)
    last_date = models.CharField(max_length=100,null=True)
    job_desc = models.CharField(max_length=100,null=True)

class Jobapply(models.Model):
    student = models.ForeignKey(Stud_Reg,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    a_status = models.CharField(max_length=100)

class PlacedStudent(models.Model):
    student = models.ForeignKey(Stud_Reg,on_delete=models.CASCADE,null=True)
    jobapply = models.ForeignKey(Jobapply,on_delete=models.CASCADE)
    company = models.ForeignKey(Reg,on_delete=models.CASCADE,null=True)
    place_status =  models.CharField(max_length=100)

class ChatStudent(models.Model):
   student = models.ForeignKey(Stud_Reg,on_delete=models.CASCADE,null=True)
   sender = models.CharField(max_length=100)
   message = models.CharField(max_length=100)
   time = models.CharField(max_length=100)
   status = models.CharField(max_length=100, null=True)



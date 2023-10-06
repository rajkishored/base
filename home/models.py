from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Job(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    shop_name = models.CharField(max_length=100,null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    discription = models.TextField(null=True)
    salary = models.FloatField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=30, null=True)
    experience = models.CharField(max_length=30, null=True)
    eduction = models.CharField(max_length=100, null=True)
    skill = models.CharField(max_length=100, null=True)
    job_link = models.URLField(null=True)
    ratings = models.IntegerField(null=True)


class Employee(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  
    adharno = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)
    photo = models.ImageField(null=True,upload_to="employeephoto/")
    emecontact = models.IntegerField(null=True)
    skill = models.CharField(max_length=100, null=True)


class Employer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    adharno = models.IntegerField(null=True)
    gender = models.CharField(max_length=10,null=True)

class Address(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    city =  models.CharField(max_length=20,null=True)
    pin = models.IntegerField(null=True)




    
       

    


     
    




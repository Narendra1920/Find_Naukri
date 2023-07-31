from django.db import models

class Student(models.Model):
    #id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()

class Cars(models.Model):
    car_name=models.CharField(max_length=100)
    car_speed=models.IntegerField()
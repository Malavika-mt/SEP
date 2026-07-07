
from django.db import models


# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    head_of_dept=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
 

class Employee(models.Model):
    name=models.CharField(max_length=100,unique=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


class Student_Register(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    department=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
     

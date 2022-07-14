from tkinter import CASCADE
from django.db import models
from user_register.models import User

# Create your models here.
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=50)
    owner_name= models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


def __str__(self):
    return self.vehicle_type
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=50)
    owner_name= models.CharField(max_length=100)
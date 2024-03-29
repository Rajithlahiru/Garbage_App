from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(max_length=50)
    mobile_no = models.IntegerField(default="")
    nic = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    type = models.CharField(max_length=255,default='DRIVER')
     
def __str__(self):
    return self.username

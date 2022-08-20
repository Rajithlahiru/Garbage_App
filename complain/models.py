from django.db import models
import email
from statistics import mode

# Create your models here.
class Complain(models.Model):
    email = models.EmailField()
    detail = models.TextField()
    

    def __str__(self):
        return self.email
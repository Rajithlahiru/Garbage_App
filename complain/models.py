from django.db import models
import email
from statistics import mode

# Create your models here.
class Complain(models.Model):
    req_id = models.CharField(max_length=255, default="")
    email = models.EmailField()
    detail = models.TextField()
    

    def __str__(self):
        return self.email
from django.db import models
import email
from statistics import mode

# Create your models here.
class complain(models.Model):
    req_id = models.IntegerField()
    email = models.EmailField()
    detail = models.TextField()

    def __str__(self):
        return self.complain_id
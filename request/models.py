from django.db import models

class Request(models.Model):
    username = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    garbage_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location

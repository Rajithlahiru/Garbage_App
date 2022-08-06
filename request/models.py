from django.db import models

class Request(models.Model):
    user = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    garbage_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status
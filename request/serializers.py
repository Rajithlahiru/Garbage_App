from dataclasses import field, fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Request
import geocoder

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    address = Request.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    class Meta:
        model = Request
        fields = ['location']

from dataclasses import field, fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Request, complain


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['location','longitude','latitude','garbage_type','status']

class ComplainSerializer(serializers.ModelSerializer):

    class Meta:
        model = complain
        field = '__all__'

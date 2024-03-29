from dataclasses import field, fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Request
from complain.models import Complain

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['location','longitude','latitude','garbage_type','status']


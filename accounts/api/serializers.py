from dataclasses import field, fields
import email
from statistics import mode
from tkinter.ttk import Style
from turtle import write
from rest_framework import serializers
from accounts.models import Accounts

class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    
    class Meta:
        model = Accounts
        fields =    ['email','username','password','password2']
        extra_kwargs ={
                'password':{'write_only':True}
        }
    
    def save(self):
        accounts = Accounts(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Password must match'})
        accounts.set_password(password)
        accounts.save()
        return accounts

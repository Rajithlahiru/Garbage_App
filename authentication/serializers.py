from cProfile import label
from dataclasses import field
import email
from pyexpat import model
from rest_framework import serializers
from user_register.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length= 4, write_only =True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')
        
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username invalid'
            )
        return attrs
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
from rest_framework import serializers
from user_register.models  import User
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model = User
            fields = ['id','username', 'email', 'password']

      def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

      def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id','username', 'email', 'password', 'mobile_no', 'nic', 'address', 'type']

class LoginSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['email', 'password']

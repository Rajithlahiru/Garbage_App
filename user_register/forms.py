from dataclasses import field
from logging import PlaceHolder
from pyexpat import model
from django import forms
from .models import User
from django.forms import ModelForm

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password','mobile_no','nic','address')
        labels = {
            'username':'UserName',
            'email':'E-mail',
            'password':'Password',
            'mobile_no':'Mobile-No',
            'nic':'NIC',
            'address':'Address'
        }

        widgets = {
            'username': forms.TextInput(attrs ={'class': 'form-control','placeholder':'Enter your name here'}),
            'email': forms.EmailInput(attrs ={'class': 'form-control','placeholder':'name@example.com'}),
            'password': forms.TextInput(attrs ={'class': 'form-control','placeholder':'Enter a password'}),
            'mobile_no': forms.TextInput(attrs ={'class': 'form-control','placeholder':'+94 *********'}),
            'nic': forms.TextInput(attrs ={'class': 'form-control','placeholder':'Enter your NIC'}),
            'address': forms.TextInput(attrs ={'class': 'form-control','placeholder':'Enter your Address'}),
        }
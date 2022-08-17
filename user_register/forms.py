from dataclasses import field
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
            'username': forms.TextInput(attrs ={'class': 'form-control'}),
            'email': forms.EmailInput(attrs ={'class': 'form-control'}),
            'password': forms.TextInput(attrs ={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs ={'class': 'form-control'}),
            'nic': forms.TextInput(attrs ={'class': 'form-control'}),
            'address': forms.TextInput(attrs ={'class': 'form-control'}),
        }
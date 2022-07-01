from dataclasses import field
from pyexpat import model
from django import forms
from .models import User

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
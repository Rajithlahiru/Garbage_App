from dataclasses import field
from logging import PlaceHolder
from django import forms
from .models import Complain
from django.forms import ModelForm

class complainForm(forms.ModelForm):

    class Meta:
        model = Complain
        fields = '__all__'
        labels = {
            'email':'E-mail',
            # 'req_id':'Request ID',
            'detail': 'Complain'
        }

        widgets = {
            'email': forms.EmailInput(attrs ={'class': 'form-control'}),
            # 'req_id': forms.TextInput(attrs={'class':'form-control'}),
            'detail': forms.Textarea(attrs={'class':'form-control'})
        }
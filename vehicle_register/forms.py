import sys
sys.path.append("..") 
from django import forms
from .models import Vehicle
from user_register.models import User


class UserListForm(forms.Form):
 
    GEEKS_CHOICES =[ ]
    users = User.objects.all()

    for data in users:
        GEEKS_CHOICES.append((data.id,data.username))

    owner_name = forms.ChoiceField(choices = GEEKS_CHOICES)

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('vehicle_type','vehicle_model','vehicle_no')
        labels = {
            'vehicle_type':'Vehicle Type',
            'vehicle_model':'Vehicle Model',
            'vehicle_no':'Vehicle Number',
            # 'owner_name':'Owner Name',
        }

        widgets = {
            'vehicle_type': forms.TextInput(attrs ={'class': 'form-control'}),
            'vehicle_model': forms.TextInput(attrs ={'class': 'form-control'}),
            'vehicle_no': forms.TextInput(attrs ={'class': 'form-control'}),
            # 'owner_name': forms.TextInput(attrs ={'class': 'form-control'}),
        }
        
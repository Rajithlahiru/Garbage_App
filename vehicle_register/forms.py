from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('vehicle_type','vehicle_model','vehicle_no','owner_name')
        labels = {
            'vehicle_type':'Vehicle Type',
            'vehicle_model':'Vehicle Model',
            'vehicle_no':'Vehicle Number',
            'owner_name':'Owner Name',
        }
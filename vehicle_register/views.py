from multiprocessing import context
import re
from django.shortcuts import redirect, render
from .forms import VehicleForm,UserListForm
from .models import Vehicle

# Create your views here.
def vehicle_list(request):
    context = {'vehicle_list':Vehicle.objects.all()}
    return render(request,'vehicle_register/vehicle_list.html',context)

def vehicle_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = VehicleForm()
            a=UserListForm()
        else:
            vehicle = Vehicle.objects.get(pk=id)
            form = VehicleForm(instance=vehicle)
            a=UserListForm()
        return render(request, 'vehicle_register/vehicle_form.html', {'form':form,'a':a})
    else:
        if id==0:
            form = VehicleForm(request.POST)
        else:
            vehicle = Vehicle.objects.get(pk=id)
            form = VehicleForm(request.POST,instance=vehicle)
        if form.is_valid():
            form.save()
        return redirect('/vehicle/list')

def vehicle_delete(request,id):
    vehicle = Vehicle.objects.get(pk=id)
    vehicle.delete()
    return redirect('/vehicle/list')

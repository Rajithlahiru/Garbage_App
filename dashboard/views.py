from django.shortcuts import render
from user_register.models import User
from vehicle_register.models import Vehicle 

# Create your views here.
def index(request):
    return render(request, 'base/base.html')

def report(request):
    return render(request, 'dashboard/reports.html')

def reports(request):
    users_count = User.objects.all().count()
    vehicle_count = Vehicle.objects.all().count()
    context = {
        'users_count':users_count,
        'vehicle_count':vehicle_count
    }
    return render(request,'dashboard/reports.html',context)

from django.shortcuts import render
from user_register.models import User
from vehicle_register.models import Vehicle
import datetime
import json
from urllib.request import urlopen

 

# Create your views here.
def index(request):
    return render(request, 'base/base.html')

def report(request):
    response = urlopen('http://127.0.0.1:8000/api/request/')
    data = json.loads(response.read())
    users_count = User.objects.all().count()
    vehicle_count = Vehicle.objects.all().count()
    var = datetime.date.today()
    formatDate = var.strftime("%d-%b-%y")
    context = {
        'users_count':users_count,
        'vehicle_count': vehicle_count,
        'formatDate':formatDate,
        'currentDate':var,
        'data':data
    }
    return render(request,'dashboard/reports.html',context)

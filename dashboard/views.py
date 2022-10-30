from django.http import JsonResponse
from django.shortcuts import render
from user_register.models import User
from vehicle_register.models import Vehicle
import datetime
import json
from urllib.request import urlopen
from request.models import Request

 

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
    collected = Request.objects.filter(status = "COLLECTED").count()
    not_collected = Request.objects.filter(status = "NOT COLLECTED").count()
    context = {
        'users_count':users_count,
        'vehicle_count': vehicle_count,
        'formatDate':formatDate,
        'currentDate':var,
        'data':data,
        'request_count':Request.objects.all().count(),
        'collected':collected,
        'not_collected': not_collected,
        
    }
    return render(request,'dashboard/reports.html',context)

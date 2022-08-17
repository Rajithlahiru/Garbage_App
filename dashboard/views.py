from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/base.html')

def report(request):
    return render(request, 'dashboard/reports.html')

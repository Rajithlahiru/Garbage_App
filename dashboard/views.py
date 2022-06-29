from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def signup(request):
    return render(request, 'dashboard/signup.html')

def signin(request):
    return render(request, 'dashboard/signin.html')
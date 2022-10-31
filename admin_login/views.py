import email
from django.shortcuts import render, redirect
from django.http import HttpRequest
from urllib import request
from operator import index
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'email taken')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'password not matching')
            return redirect('signup') 

    else:
        return render(request,"admin_login/signup.html")


# def signin(request):

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(email = email, password = password)

#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.info(request, 'credentials invalid')
#             return redirect('signin')

#     else:
#         return render(request, 'admin_login/signin.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == 'admin@gmail.com' and password == 'password':
            return redirect('dashboard/report')

    else:        
        return render(request, 'admin_login/signin.html')


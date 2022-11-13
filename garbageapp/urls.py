"""garbageapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('user/', include('user_register.urls')),
    path('vehicle/', include('vehicle_register.urls')),
    path('complain/', include('complain.urls')),
    path('', include('admin_login.urls')),
    path('request_list', include('request_list.urls')),

    #REST FRAMEWORK URLS
    path('api/', include('request.urls')),
    path('api/auth/', include('authentication.urls')),

    # path('register/', include('authentication.urls')),
    path('',include('garbage.urls')),
]




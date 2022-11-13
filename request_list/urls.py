from django.urls import path
from .import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
]

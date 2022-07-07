from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_map, name='show_map'),
]
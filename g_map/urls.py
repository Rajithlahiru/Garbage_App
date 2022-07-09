from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_gmap,name="show_gmap"),
]
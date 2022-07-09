from django.urls import path
from .import views

urlpatterns =[
    path('',views.RequestList.as_view()),
    path('locations/',views.LocationApi.as_view()),
]
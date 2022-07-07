from django.urls import path
from .import views

urlpatterns =[
    path('',views.RequestList.as_view()),
]
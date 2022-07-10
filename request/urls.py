from django.urls import path
from .import views

urlpatterns =[
    path('request/',views.RequestList.as_view()),
    path('request/locations/',views.LocationApi.as_view()),
    path('request/<int:pid>',views.RequestDetails.as_view()),
]
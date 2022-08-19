from django.urls import path
from .import views

urlpatterns =[
    path('request/',views.Request.as_view()),
    # path('request/locations/',views.LocationApi.as_view()),
    path('request/<int:pk>',views.Request.as_view()),
    path('request/complain',views.Complain.as_view()),
]
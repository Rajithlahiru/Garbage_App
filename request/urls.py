from django.urls import path
from .import views


urlpatterns =[
    path('request/',views.Request.as_view()),
    # path('request/locations/',views.LocationApi.as_view()),
    path('request/<int:pk>',views.Request.as_view()),
    # path('count/',views.RequestCount.as_view()),

    path('complain/',views.Complain.as_view()),
    # path('request/locations/',views.LocationApi.as_view()),
    path('complain/<int:pk>',views.Complain.as_view()),
    # path('count/',views.RequestCount.as_view()),

    path('image/',views.ImageClasifier.as_view()),
]
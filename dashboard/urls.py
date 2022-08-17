from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="dashboard"),
    path('report/',views.report, name="report")
]
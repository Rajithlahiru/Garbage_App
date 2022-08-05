from django.urls import path
from .import views

urlpatterns = [
    path('garbage_list/',views.GarbageList.as_view()),
]
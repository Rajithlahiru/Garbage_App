from django import views
from django.urls import path
from . import views

urlpatterns = [
    # path("signup", views.signup, name='signup'),
    path("", views.signin, name='signin'),
]
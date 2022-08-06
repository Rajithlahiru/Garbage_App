from atexit import register
from django.urls import path
from .views import RegisterView,Register,Login

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
]
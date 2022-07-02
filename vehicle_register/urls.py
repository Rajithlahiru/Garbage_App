from django.urls import path
from .import views

urlpatterns = [
    path('', views.vehicle_form, name='vehicle_insert'),
    path('<int:id>/', views.vehicle_form, name='vehicle_update'),
    path('delete/<int:id>/', views.vehicle_delete, name='vehicle_delete'),
    path('list/', views.vehicle_list, name='vehicle_list'),

]

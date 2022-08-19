from django.urls import path
from .import views

urlpatterns =[
    path('', views.complain_form, name='complain_insert'),
    path('<int:id>/', views.complain_form, name='complain_update'),
    path('delete/<int:id>/', views.complain_delete, name='complain_delete'),
    path('list/', views.complain_list, name='complain_list'),
]
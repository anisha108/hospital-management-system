from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('toggle/<int:id>/', views.toggle_doctor, name='toggle_doctor'),
]
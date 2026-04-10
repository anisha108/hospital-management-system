from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointments_list, name='appointments'),
    path("add/", views.add_appointment, name="add_appointment"),
    path('update/<int:id>/', views.update_appointment, name='update_appointment'),
]
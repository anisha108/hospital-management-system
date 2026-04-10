from django.urls import path
from . import views

urlpatterns = [
    path("", views.patients_list, name="patients"),
    path("add/", views.add_patient, name="add_patient"),
]
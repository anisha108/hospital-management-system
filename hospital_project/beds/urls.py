from django.urls import path
from . import views

urlpatterns = [
    path('', views.bed_list, name='bed_list'),
    path('add/', views.add_bed, name='add_bed'),
    path('bed/<int:id>/', views.bed_detail, name='bed_detail'),
]
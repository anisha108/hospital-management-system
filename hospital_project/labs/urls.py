from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_results, name='lab_results'),
    path('lab-result/<int:id>/', views.lab_result_detail, name='lab_result_detail'),
]
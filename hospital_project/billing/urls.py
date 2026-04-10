from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_home, name='billing_home'),
    path('create/', views.create_bill, name='create_bill'),
    path('view/<int:id>/', views.view_bill, name='view_bill'),
]
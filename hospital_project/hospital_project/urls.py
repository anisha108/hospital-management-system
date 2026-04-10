from django.contrib import admin
from django.urls import path, include
from dashboard import views  # or wherever your dashboard view is

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctors.urls')),
    path('', include('dashboard.urls')),
    path("patients/", include("patients.urls")),
    path('', views.dashboard, name='dashboard'),
    path('appointments/', include('appointments.urls')),
    path('beds/', include('beds.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('billing/', include('billing.urls')),
   path('labs/', include('labs.urls')),
]
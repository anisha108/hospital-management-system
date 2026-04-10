from django.shortcuts import render
from .models import Doctor
from django.shortcuts import redirect, get_object_or_404

def toggle_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    doctor.is_available = not doctor.is_available  # ✅ toggle
    doctor.save()

    return redirect('doctors_list')

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors': doctors})
from django.shortcuts import render
from .models import Patient

def patients_list(request):
    query = request.GET.get('q')  # get search input

    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()

    context = {
        'patients': patients,
        'query': query
    }

    return render(request, 'patients/patients.html', context)

from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm


def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patients")
    else:
        form = PatientForm()

    return render(request, "patients/add_patient.html", {"form": form})
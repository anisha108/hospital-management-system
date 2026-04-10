from django.shortcuts import render, redirect
from .models import Bed
from .forms import BedForm


def bed_list(request):
    beds = Bed.objects.all().order_by("floor", "bed_number")

    floors = {}
    for bed in beds:
        floors.setdefault(bed.floor, []).append(bed)

    floors = dict(sorted(floors.items()))  # ✅ SORT FLOORS

    total = beds.count()
    occupied = beds.filter(status="Occupied").count()

    return render(request, 'beds/bed_list.html', {
        'floors': floors,
        'total': total,
        'occupied': occupied
    })

def add_bed(request):
    if request.method == 'POST':
        form = BedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bed_list')
    else:
        form = BedForm()
    return render(request, 'beds/add_bed.html', {'form': form})

from patients.models import Patient

def bed_detail(request, id):
    bed = Bed.objects.get(id=id)
    patients = Patient.objects.exclude(bed__isnull=False)

    if request.method == 'POST':
        status = request.POST.get('status')
        patient_id = request.POST.get('patient')

        bed.status = status

        if status == "Occupied" and patient_id:
            patient = Patient.objects.get(id=patient_id)

            Bed.objects.filter(patient=patient).exclude(id=bed.id).update(
                patient=None,
                status="Available"
            )

            bed.patient = patient
        else:
            bed.patient = None

        bed.save()
        return redirect('bed_list')

    return render(request, 'beds/bed_detail.html', {
        'bed': bed,
        'patients': patients
    })
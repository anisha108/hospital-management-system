from django.shortcuts import render, redirect
from .models import LabResult, LabTest
from patients.models import Patient
from django.http import JsonResponse

def lab_result_detail(request, id):
    r = LabResult.objects.select_related('patient', 'test').get(id=id)

    return JsonResponse({
        'patient': r.patient.name,
        'test': r.test.name,
        'result': r.result,
        'range': r.test.normal_range,
    })

def lab_results(request):
    results = LabResult.objects.select_related('patient', 'test')
    patients = Patient.objects.all()
    tests = LabTest.objects.all()

    # Handle adding new test
    if request.method == "POST":
        patient_id = request.POST.get('patient')
        test_id = request.POST.get('test')
        status = request.POST.get('status')
        result = request.POST.get('result', '')

        LabResult.objects.create(
            patient_id=patient_id,
            test_id=test_id,
            status=status,
            result=result
        )

        return redirect('lab_results')

    return render(request, 'labs/lab_results.html', {
        'results': results,
        'patients': patients,
        'tests': tests
    })
from django.shortcuts import render,redirect
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Bill
from django.db.models import Sum
from datetime import date
from django.db.models import Count
from django.db.models.functions import TruncMonth
import json


def dashboard(request):
    monthly_data = (
    Appointment.objects
    .annotate(month=TruncMonth('date'))
    .values('month')
    .annotate(count=Count('id'))
    .order_by('month')
)

    months = [entry['month'].strftime('%b') for entry in monthly_data]
    counts = [entry['count'] for entry in monthly_data]
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    appointments_today = Appointment.objects.filter(date=date.today()).count()

    total_revenue = Bill.objects.aggregate(
        total=Sum('final_amount')
    )['total'] or 0

    # Critical patients
    critical_patients = Patient.objects.filter(status="Critical")

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'appointments_today': appointments_today,
        'total_revenue': total_revenue,
        'critical_patients': critical_patients,
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'months': json.dumps(months),
        'counts': json.dumps(counts),

    }

    return render(request, 'dashboard.html', context)
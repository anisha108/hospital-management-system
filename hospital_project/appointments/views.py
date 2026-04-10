from django.shortcuts import render,redirect
from .models import Appointment
from .forms import AppointmentForm
from datetime import date, timedelta

def appointments_list(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    third_day = today + timedelta(days=2)

    selected_date = request.GET.get('date')

    if selected_date:
        appointments = Appointment.objects.filter(date=selected_date)
    else:
        appointments = Appointment.objects.filter(date=today)

    context = {
        'appointments': appointments,
        'today': today,
        'tomorrow': tomorrow,
        'third_day': third_day,
    }

    return render(request, 'appointments/appointments.html', context)

def appointments_list(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    next_day = today + timedelta(days=2)

    selected_date = request.GET.get("date")

    if selected_date:
        appointments = Appointment.objects.filter(date=selected_date)
    else:
        appointments = Appointment.objects.filter(date=today)

    context = {
        "appointments": appointments,
        "today": today,
        "tomorrow": tomorrow,
        "next_day": next_day,
        "selected_date": selected_date,
    }

    return render(request, "appointments/appointments.html", context)

def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.status = "Scheduled" 
            form.save()
            return redirect("appointments")
    else:
        form = AppointmentForm()

    return render(request, "appointments/add_appointment.html", {"form": form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment

def update_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == 'POST':
        status = request.POST.get('status')
        appointment.status = status
        appointment.save()
        return redirect('appointments')

    return render(request, 'appointments/update_appointment.html', {
        'appointment': appointment
    })
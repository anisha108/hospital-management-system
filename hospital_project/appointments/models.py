from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError("Date cannot be in the past.")
    

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('In Progress', 'In Progress'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    TYPE_CHOICES = [
        ('Follow-up', 'Follow-up'),
        ('Checkup', 'Checkup'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateField(validators=[validate_future_date])
    time = models.TimeField()
    status = models.CharField(max_length=20, default="Scheduled")
    def __str__(self):
        return f"{self.patient.name} - {self.date} {self.time}"
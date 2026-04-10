from django.db import models
from patients.models import Patient

class LabTest(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    normal_range = models.CharField(max_length=100)

class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    result = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # Completed / Critical / In Progress
    date = models.DateField(auto_now_add=True)
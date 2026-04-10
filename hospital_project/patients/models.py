from django.db import models

class Patient(models.Model):
    STATUS_CHOICES = [
        ("Admitted", "Admitted"),
        ("Critical", "Critical"),
        ("Outpatient", "Outpatient"),
        ("Discharged", "Discharged"),
    ]

    name = models.CharField(max_length=100, default="Unknown")
    age = models.IntegerField() 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
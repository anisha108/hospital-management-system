from django.db import models
from patients.models import Patient
class Bed(models.Model):

    STATUS_CHOICES = [
        ("Occupied", "Occupied"),
        ("Available", "Available"),
        ("Reserved", "Reserved"),
    ]

    bed_number = models.CharField(max_length=10, unique=True)

    # Default values
    department = models.CharField(max_length=50, default="General")
    floor = models.CharField(max_length=20, default="One")

    # Only Admitted patients can be assigned
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'status': 'Admitted'}
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )

    def save(self, *args, **kwargs):
        """
        Auto-manage bed status:
        - If patient assigned → Occupied
        - If patient removed AND status was Occupied → Available
        - Maintenance and Reserved remain untouched
        """
        if self.patient:
            self.status = "Occupied"
        elif self.status == "Occupied":
            self.status = "Available"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bed {self.bed_number} - {self.department} (Floor {self.floor})"
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    patients_count = models.IntegerField()
    experience_years = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
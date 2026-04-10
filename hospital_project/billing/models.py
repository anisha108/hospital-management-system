from django.db import models
from patients.models import Patient

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    invoice_number = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        # Save first to get ID
        super().save(*args, **kwargs)

        # Generate invoice number if not present
        if not self.invoice_number:
            self.invoice_number = f"INV-{str(self.id).zfill(4)}"
            super().save(update_fields=['invoice_number'])

    def __str__(self):
        return f"{self.invoice_number} - {self.patient.name}"


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.price * self.quantity

    def __str__(self):
        return self.description
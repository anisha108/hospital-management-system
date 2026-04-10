from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100,unique=True)
    manufacturer = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.medicine.name
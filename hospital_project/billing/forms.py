from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'})
        }
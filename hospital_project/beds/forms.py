from django import forms
from .models import Bed

class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = '__all__'
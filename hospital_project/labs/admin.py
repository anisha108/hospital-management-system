from django.contrib import admin
from .models import LabTest, LabResult

admin.site.register(LabTest)
admin.site.register(LabResult)
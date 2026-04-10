from django.contrib import admin
from .models import Bed

admin.site.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('bed_number', 'department', 'floor', 'patient', 'status')
    list_filter = ('status', 'floor')
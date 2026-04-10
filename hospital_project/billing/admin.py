from django.contrib import admin
from .models import Bill, BillItem


class BillItemInline(admin.TabularInline):
    model = BillItem
    extra = 1


class BillAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'patient', 'date', 'final_amount')
    search_fields = ('patient__name', 'invoice_number')
    list_filter = ('date',)
    inlines = [BillItemInline]


admin.site.register(Bill, BillAdmin)
admin.site.register(BillItem)
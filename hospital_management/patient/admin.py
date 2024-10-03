from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientModelAdmin(admin.ModelAdmin):
    list_display = ['name','phone']

    def name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    
admin.site.register(Patient, PatientModelAdmin)
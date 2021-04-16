from django.contrib import admin
from patient.models import Patient
from patient.import_export_resources import PatientResource

from import_export.admin import ImportExportModelAdmin


class PatientAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Patient._meta.get_fields()]
    resource_class = PatientResource


admin.site.register(Patient, PatientAdmin)

from import_export import resources

from patient.models import Patient


class PatientResource(resources.ModelResource):

    class Meta:
        model = Patient
        exclude = ("pk",)

from patient.models import Patient

from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        read_only_fields = ('id',)
        fields = "__all__"

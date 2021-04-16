from hospital.models import HospitalCapabilities, Hospital
from patient.serializers import PatientSerializer

from rest_framework import serializers


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        read_only_fields = ('id',)
        fields = "__all__"


class HospitalCapabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalCapabilities
        read_only_fields = ('id',)
        fields = "__all__"


class TargetHospitalSerializer(serializers.Serializer):
    patient = PatientSerializer()
    best_hospital = HospitalSerializer()
    ai_detection = serializers.CharField()
    best_path = serializers.ListField(serializers.CharField(read_only=True))
    shortest_path = serializers.ListField(serializers.CharField(read_only=True))
    total_cost = serializers.IntegerField()

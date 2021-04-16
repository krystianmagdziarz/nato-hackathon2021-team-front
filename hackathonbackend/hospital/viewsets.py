from hospital.models import Hospital, HospitalCapabilities
from hospital.serializers import HospitalSerializer, HospitalCapabilitiesSerializer

from rest_framework import viewsets


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalCapabilitiesViewSet(viewsets.ModelViewSet):
    queryset = HospitalCapabilities.objects.all()
    serializer_class = HospitalCapabilitiesSerializer


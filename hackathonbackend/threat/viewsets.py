from threat.models import Threat
from threat.serializers import ThreatSerializer

from rest_framework import viewsets


class ThreatViewSet(viewsets.ModelViewSet):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer



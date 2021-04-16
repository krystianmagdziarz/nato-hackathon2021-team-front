from threat.models import Threat

from rest_framework import serializers


class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        read_only_fields = ('id',)
        fields = "__all__"

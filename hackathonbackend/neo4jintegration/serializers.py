from rest_framework import serializers


class PointsSerializer(serializers.Serializer):
    points = serializers.ListField(serializers.CharField(read_only=True))

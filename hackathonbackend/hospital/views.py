from django.shortcuts import render
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['PUT'])
def partial_update_civilian_hospital(request):
    try:
        hospital = Hospital.objects.filter(name="Civilian Hospital").first()
        if request.method == 'PUT':
            serializer = HospitalSerializer(hospital, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=402)
    except Exception:
        return Response(status=401)
    return Response(status=200)

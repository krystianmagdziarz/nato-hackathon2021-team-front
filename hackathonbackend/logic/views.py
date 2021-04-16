from django.http import HttpResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response

from neo4jintegration.views import calculate_shortest_node_path, calculate_shortest_path_time

from hospital.serializers import TargetHospitalSerializer

from patient.models import Patient

from logic.decision_tree import DecisionTree

import datetime


@api_view()
def target_hospital(request, patient_id):

    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return HttpResponse(status=400)

    if patient.grid_x is not None and patient.grid_y is not None:
        if str(patient.immediate_return_to_duty).lower() == "yes" or \
                str(patient.category).lower() == "minimal" or \
                str(patient.category).lower() == "espectant":
            # Zwracam statuc_code = 205 w przypadku gdy pomóc ma kolega
            # Buddy help
            return HttpResponse(status=205)

        dt = DecisionTree(patient=patient)
        DecisionTree.normalize_data()
        dt.evacuatePatient()

        result = calculate_shortest_node_path(
            patient.grid_x + patient.grid_y,
            patient.selected_hospital.grid_x + patient.selected_hospital.grid_y
        )
        best_path = result["nodeNames"]
        best_cost = result["totalCost"]

        patient.transport_date_start = timezone.now()
        time_change = datetime.timedelta(minutes=best_cost)
        patient.transport_date_end = patient.transport_date_start + time_change
        patient.save()

        shortest_path_time_to_this_hospital = calculate_shortest_path_time(
            patient.grid_x+patient.grid_y,
            patient.selected_hospital.grid_x + patient.selected_hospital.grid_y)["nodeNames"]

        try:
            notify_commander(patient)
            notify_hospital(patient)
        except Exception as e:
            pass

        serializer = TargetHospitalSerializer({
            "patient": patient,
            "best_hospital": patient.selected_hospital,
            "ai_detection": dt.ai_detection,
            "best_path": best_path,
            "shortest_path": shortest_path_time_to_this_hospital,
            "total_cost": best_cost
        })
        return Response(serializer.data)
    return Response(status=401)


def notify_about_patient(message, receiver):
    from django.core.mail import send_mail

    send_mail(
        'New wounded',
        message,
        'kry.magdziarz@ron.mil.pl',
        [receiver],
        fail_silently=False,
    )


def notify_commander(patient):
    message_text = f"ATTENTION! Dear Commander, our soldier has suffered. Support needed. Patient id: {patient.pk}"
    notify_about_patient(message_text, 'kry.magdziarz@ron.mil.pl')


def notify_hospital(patient):
    # For all hostpital e-mail will be sent to one mail for dev purposes
    message_text = f"ATTENTION! A new soldier needs medical attention! " \
                   f"Please prepare yourselves! Patient id: {patient.pk}"
    notify_about_patient(message_text, 'kry.magdziarz@ron.mil.pl')

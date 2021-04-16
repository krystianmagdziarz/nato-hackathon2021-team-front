from hospital.models import Hospital
from django.db import models


class Patient(models.Model):
    scenario = models.CharField("Scenario", max_length=255, null=True, blank=True)
    patient_id = models.CharField("Patient id", max_length=255, null=True, blank=True)
    category = models.CharField("Category", max_length=255, null=True, blank=True)
    patient_type = models.CharField("Patient type", max_length=255, null=True, blank=True)
    location = models.CharField("Location", max_length=255, null=True, blank=True)
    mechanism_of_injury = models.CharField("Mechanism of injury", max_length=255, null=True, blank=True)
    injury = models.CharField("Injury", max_length=255, null=True, blank=True)
    course_of_action = models.CharField("Course of action", max_length=255, null=True, blank=True)
    surgery = models.CharField("Surgery", max_length=255, null=True, blank=True)
    immediate_return_to_duty = models.CharField("Immediate return to duty", max_length=255, null=True, blank=True)
    triage = models.CharField("Triage", max_length=255, null=True, blank=True)
    expected_days_hold = models.CharField("Expected days hold", max_length=255, null=True, blank=True)
    notes = models.CharField("Notes", max_length=255, null=True, blank=True)

    grid_x = models.CharField("X position on the map", max_length=2, null=True, blank=True)
    grid_y = models.CharField("Y position on the map", max_length=2, null=True, blank=True)

    transport_date_start = models.DateTimeField("Date of start", null=True, blank=True)
    transport_date_end = models.DateTimeField("Date of arrival to hospital", null=True, blank=True)

    selected_hospital = models.ForeignKey(Hospital, null=True, blank=True, on_delete=models.SET_NULL)

    tried_evacute_immediate_with_result = models.BooleanField(default=False)
    patient_transported_to_hospital_with_free_beds = models.BooleanField(default=False)
    patient_transported_to_hospital_with_specializations = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


from django.db.models.signals import post_save
from django.dispatch import receiver
from hospital.models import HospitalCapabilities


@receiver(post_save, sender=HospitalCapabilities)
def after_hc_created(sender, instance, created, **kwargs):
    if created:
        instance.specialized_first_aid = True
        instance.resucitation = True
        instance.stabilization = True
        instance.minor_aid_for_immediate_return_to_duty = True
        instance.initial_stress_management = True
        instance.primary_disease_prevention = True
        instance.prep_of_casulaties_for_evacuation_to_higher_level_treatment = True
        instance.emergency_dental_care = True
        instance.establish_cause_of_death = True
        instance.basic_laboratory_testing = True
        instance.patient_holding = True
        instance.xrays = True
        instance.damage_control_surgery = True
        instance.enhanced_laboratory_testing = True
        instance.dental = True
        instance.isolation_ward = True
        instance.shock_treatment = True
        instance.mental_health = True
        instance.intensive_care_unit = True
        instance.ctscan = True
        instance.prepare_patient_for_aeromed_evactuation = True
        instance.specialized_surgery = True
        instance.emergency_gynaecological = True
        instance.dental_surgery = True
        instance.longterm_patient_holding = True
        instance.reconstructive_surgery = True
        instance.blood_bank = True
        instance.mortuary = True

        if instance.type == "A":
            instance.patient_holding = False
            instance.xrays = False
            instance.damage_control_surgery = False
            instance.enhanced_laboratory_testing = False
            instance.dental = False
            instance.isolation_ward = False
            instance.shock_treatment = False
            instance.mental_health = False
            instance.intensive_care_unit = False
            instance.ctscan = False
            instance.prepare_patient_for_aeromed_evactuation = False
            instance.specialized_surgery = False
            instance.emergency_gynaecological = False
            instance.dental_surgery = False
            instance.longterm_patient_holding = False
            instance.reconstructive_surgery = False
            instance.blood_bank = False
            instance.mortuary = False
        elif instance.type == "B":
            instance.enhanced_laboratory_testing = False
            instance.dental = False
            instance.isolation_ward = False
            instance.shock_treatment = False
            instance.mental_health = False
            instance.intensive_care_unit = False
            instance.ctscan = False
            instance.prepare_patient_for_aeromed_evactuation = False
            instance.specialized_surgery = False
            instance.emergency_gynaecological = False
            instance.dental_surgery = False
            instance.longterm_patient_holding = False
            instance.reconstructive_surgery = False
            instance.blood_bank = False
            instance.mortuary = False
        elif instance.type == "C":
            instance.specialized_surgery = False
            instance.emergency_gynaecological = False
            instance.dental_surgery = False
            instance.longterm_patient_holding = False
            instance.reconstructive_surgery = False
            instance.blood_bank = False
            instance.mortuary = False
        elif instance.type == "D":
            pass

        instance.save()

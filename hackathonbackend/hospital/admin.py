from django.contrib import admin
from hospital.models import HospitalCapabilities, Hospital


@admin.register(HospitalCapabilities)
class HospitalCapabilitiesAdmin(admin.ModelAdmin):
    list_display = ('type',)
    readonly_fields = (
        'specialized_first_aid',
        'resucitation',
        'stabilization',
        'minor_aid_for_immediate_return_to_duty',
        'initial_stress_management',
        'primary_disease_prevention',
        'prep_of_casulaties_for_evacuation_to_higher_level_treatment',
        'emergency_dental_care',
        'establish_cause_of_death',
        'basic_laboratory_testing',
        'patient_holding',
        'xrays',
        'damage_control_surgery',
        'enhanced_laboratory_testing',
        'dental',
        'isolation_ward',
        'shock_treatment',
        'mental_health',
        'intensive_care_unit',
        'ctscan',
        'prepare_patient_for_aeromed_evactuation',
        'specialized_surgery',
        'emergency_gynaecological',
        'dental_surgery',
        'longterm_patient_holding',
        'reconstructive_surgery',
        'blood_bank',
        'mortuary',
    )


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'free_patient', 'free_beds',)


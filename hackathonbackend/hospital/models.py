from django.db import models


class HospitalCapabilities(models.Model):
    TYPES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    )

    type = models.CharField(choices=TYPES, default=TYPES[0][0], max_length=1)

    specialized_first_aid = models.BooleanField("Specialized First Aid", default=False)
    resucitation = models.BooleanField("Resucitation", default=False)
    stabilization = models.BooleanField("Stabilization", default=False)
    minor_aid_for_immediate_return_to_duty = models.BooleanField("Minor aid for immediate return to duty", default=False)
    initial_stress_management = models.BooleanField("Initial Stress Management", default=False)
    primary_disease_prevention = models.BooleanField("Primary disease prevention", default=False)
    prep_of_casulaties_for_evacuation_to_higher_level_treatment = models.BooleanField("Prep of casulaties for "
                                                                                      "evacuation to higher level "
                                                                                      "treatment", default=False)
    emergency_dental_care = models.BooleanField("Emergency dental care", default=False)
    establish_cause_of_death = models.BooleanField("Establish cause of death", default=False)
    basic_laboratory_testing = models.BooleanField("Basic Laboratory Testing", default=False)
    patient_holding = models.BooleanField("Patient holding", default=False)
    xrays = models.BooleanField("X-Rays", default=False)
    damage_control_surgery = models.BooleanField("Damage control surgery", default=False)
    enhanced_laboratory_testing = models.BooleanField("Enhanced Laboratory Testing", default=False)
    dental = models.BooleanField("Dental", default=False)
    isolation_ward = models.BooleanField("Isolation Ward", default=False)
    shock_treatment = models.BooleanField("Shock treatment", default=False)
    mental_health = models.BooleanField("Mental health", default=False)
    intensive_care_unit = models.BooleanField("Intensive Care Unit", default=False)
    ctscan = models.BooleanField("CT-scan", default=False)
    prepare_patient_for_aeromed_evactuation = models.BooleanField("Prepare patient for aeromed evactuation",
                                                                  default=False)
    specialized_surgery = models.BooleanField("Specialized surgery", default=False)
    emergency_gynaecological = models.BooleanField("Emergency gynaecological/obstretic care", default=False)
    dental_surgery = models.BooleanField("Dental surgery", default=False)
    longterm_patient_holding = models.BooleanField("Long-term patient holding", default=False)
    reconstructive_surgery = models.BooleanField("Reconstructive surgery", default=False)
    blood_bank = models.BooleanField("Blood bank", default=False)
    mortuary = models.BooleanField("Mortuary", default=False)

    def __str__(self):
        return self.type

    def check_correct_type(self, label):
        if label == 'stress':
            return self.initial_stress_management or self.shock_treatment or self.mental_health
        elif label == 'buddy help':
            return True
        elif label == 'specialized_first_aid':
            return self.specialized_first_aid
        elif label == 'resucitation':
            return self.resucitation
        elif label == 'stabilization':
            return self.stabilization
        elif label == 'minor_aid_for_immediate_return_to_duty':
            return self.minor_aid_for_immediate_return_to_duty
        elif label == 'primary_disease_prevention':
            return self.primary_disease_prevention
        elif label == 'prep_of_casulaties_for_evacuation_to_higher_level_treatment':
            return self.prep_of_casulaties_for_evacuation_to_higher_level_treatment
        elif label == 'emergency_dental_care':
            return self.emergency_dental_care
        elif label == 'establish_cause_of_death':
            return self.establish_cause_of_death
        elif label == 'basic_laboratory_testing':
            return self.basic_laboratory_testing
        elif label == 'patient_holding':
            return self.patient_holding
        elif label == 'xrays':
            return self.xrays
        elif label == 'damage_control_surgery':
            return self.damage_control_surgery
        elif label == 'enhanced_laboratory_testing':
            return self.enhanced_laboratory_testing
        elif label == 'dental':
            return self.dental
        elif label == 'isolation_ward':
            return self.isolation_ward
        elif label == 'intensive_care_unit':
            return self.intensive_care_unit
        elif label == 'ctscan':
            return self.ctscan
        elif label == 'prepare_patient_for_aeromed_evactuation':
            return self.prepare_patient_for_aeromed_evactuation
        elif label == 'specialized_surgery':
            return self.specialized_surgery
        elif label == 'emergency_gynaecological':
            return self.emergency_gynaecological
        elif label == 'dental_surgery':
            return self.dental_surgery
        elif label == 'reconstructive_surgery':
            return self.reconstructive_surgery
        elif label == 'blood_bank':
            return self.blood_bank
        elif label == 'mortuary':
            return self.mortuary
        else:
            return False


class Hospital(models.Model):
    name = models.CharField("Name", max_length=255)
    type = models.ForeignKey(HospitalCapabilities, null=True, blank=True, on_delete=models.SET_NULL)
    patient_capacity = models.PositiveIntegerField("Patient capacity")
    patients_at_the_start = models.PositiveIntegerField("No. of patients at the start")
    free_patient = models.IntegerField("FREE patients")
    total_beds_for_patient_holding = models.PositiveIntegerField("Total beds for patient holding")
    total_beds_occupied = models.PositiveIntegerField("Total beds occupied")
    free_beds = models.IntegerField("FREE beds")
    total_operating_tables = models.PositiveIntegerField("Total operating tables")

    grid_x = models.CharField("X position on the map", max_length=2)
    grid_y = models.CharField("Y position on the map", max_length=2)

    def save(self, *args, **kwargs):
        if self.patients_at_the_start > self.patient_capacity:
            self.patient_capacity = self.patients_at_the_start
        self.free_patient = self.patient_capacity - self.patients_at_the_start
        if self.total_beds_occupied > self.total_beds_for_patient_holding:
            self.total_beds_for_patient_holding = self.total_beds_occupied
        self.free_beds = self.total_beds_for_patient_holding - self.total_beds_occupied
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_type(self):
        return self.type.type

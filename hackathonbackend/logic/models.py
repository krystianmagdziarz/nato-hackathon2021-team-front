from django.db import models


class TrainData(models.Model):
    OPTIONS = (
        ('stress', 'stress'),
        ('buddy help', 'buddy help'),

        ('specialized_first_aid', 'specialized_first_aid'),
        ('resucitation', 'resucitation'),
        ('stabilization', 'stabilization'),
        ('minor_aid_for_immediate_return_to_duty', 'minor_aid_for_immediate_return_to_duty'),
        ('primary_disease_prevention', 'primary_disease_prevention'),
        ('prep_of_casulaties_for_evacuation_to_higher_level_treatment',
         'prep_of_casulaties_for_evacuation_to_higher_level_treatment'),
        ('emergency_dental_care', 'emergency_dental_care'),
        ('establish_cause_of_death', 'establish_cause_of_death'),
        ('basic_laboratory_testing', 'basic_laboratory_testing'),
        ('patient_holding', 'patient_holding'),
        ('xrays', 'xrays'),
        ('damage_control_surgery', 'damage_control_surgery'),
        ('enhanced_laboratory_testing', 'enhanced_laboratory_testing'),
        ('dental', 'dental'),
        ('isolation_ward', 'isolation_ward'),
        ('intensive_care_unit', 'intensive_care_unit'),
        ('ctscan', 'ctscan'),
        ('prepare_patient_for_aeromed_evactuation', 'prepare_patient_for_aeromed_evactuation'),
        ('specialized_surgery', 'specialized_surgery'),
        ('emergency_gynaecological', 'emergency_gynaecological'),
        ('dental_surgery', 'dental_surgery'),
        ('reconstructive_surgery', 'reconstructive_surgery'),
        ('blood_bank', 'blood_bank'),
        ('mortuary', 'mortuary'),
    )

    data = models.TextField()
    target_category = models.CharField(max_length=255, choices=OPTIONS, default=OPTIONS[0])

    def save(self, *args, **kwargs):
        self.data = str(self.data).lower()
        self.target_category = str(self.target_category).lower()
        super().save(*args, *kwargs)

    def __str__(self):
        return f"{self.data} - {self.target_category}"

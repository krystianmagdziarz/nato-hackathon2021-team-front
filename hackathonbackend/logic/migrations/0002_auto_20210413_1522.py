# Generated by Django 3.2 on 2021-04-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traindata',
            name='data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='traindata',
            name='target_category',
            field=models.CharField(choices=[('stress', 'stress'), ('buddy help', 'buddy help'), ('specialized_first_aid', 'specialized_first_aid'), ('resucitation', 'resucitation'), ('stabilization', 'stabilization'), ('minor_aid_for_immediate_return_to_duty', 'minor_aid_for_immediate_return_to_duty'), ('primary_disease_prevention', 'primary_disease_prevention'), ('prep_of_casulaties_for_evacuation_to_higher_level_treatment', 'prep_of_casulaties_for_evacuation_to_higher_level_treatment'), ('emergency_dental_care', 'emergency_dental_care'), ('establish_cause_of_death', 'establish_cause_of_death'), ('basic_laboratory_testing', 'basic_laboratory_testing'), ('patient_holding', 'patient_holding'), ('xrays', 'xrays'), ('damage_control_surgery', 'damage_control_surgery'), ('enhanced_laboratory_testing', 'enhanced_laboratory_testing'), ('dental', 'dental'), ('isolation_ward', 'isolation_ward'), ('intensive_care_unit', 'intensive_care_unit'), ('ctscan', 'ctscan'), ('prepare_patient_for_aeromed_evactuation', 'prepare_patient_for_aeromed_evactuation'), ('specialized_surgery', 'specialized_surgery'), ('emergency_gynaecological', 'emergency_gynaecological'), ('dental_surgery', 'dental_surgery'), ('reconstructive_surgery', 'reconstructive_surgery'), ('blood_bank', 'blood_bank'), ('mortuary', 'mortuary')], default=('stress', 'stress'), max_length=255),
        ),
    ]

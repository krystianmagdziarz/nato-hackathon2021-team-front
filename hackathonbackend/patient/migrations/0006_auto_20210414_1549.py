# Generated by Django 3.2 on 2021-04-14 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20210413_1929'),
        ('patient', '0005_auto_20210413_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='selected_hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hospital'),
        ),
        migrations.AddField(
            model_name='patient',
            name='transport_date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of arrival to hospital'),
        ),
        migrations.AddField(
            model_name='patient',
            name='transport_date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of start'),
        ),
    ]
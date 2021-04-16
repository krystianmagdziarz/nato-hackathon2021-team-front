# Generated by Django 3.2 on 2021-04-12 18:00
import os
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        # DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
        # DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        # DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

        DJANGO_SU_NAME = "hackathon_admin"
        DJANGO_SU_EMAIL = "krystianmagdziarz@gmail.com"
        DJANGO_SU_PASSWORD = "zgfIdjXxNFVEyrua9cjI"

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)
        superuser.is_active = True
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]


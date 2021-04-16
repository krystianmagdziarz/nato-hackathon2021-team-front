"""hackathonbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from hospital.viewsets import HospitalViewSet, HospitalCapabilitiesViewSet
from patient.viewsets import PatientViewSet
from threat.viewsets import ThreatViewSet
from neo4jintegration.views import neo4j_shortest_path, neo4j_update_node_value

from logic.views import target_hospital
from hospital.views import partial_update_civilian_hospital

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hospital', HospitalViewSet)
router.register(r'hospital-capabilities', HospitalCapabilitiesViewSet)

router.register(r'patient', PatientViewSet)

router.register(r'threat', ThreatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('patient/<int:patient_id>/target-hospital/', target_hospital, name="target-hospital"),
    path('neo4j_shortest_path/<str:node1>/<str:node2>/', neo4j_shortest_path, name="neo4j_shortest_path"),
    path('neo4j_update_node_values/<str:node1>/<int:distance>/', neo4j_update_node_value, name="neo4j_update_node_value"),
    path('partial-update-civilian-hospital/', partial_update_civilian_hospital,
         name="partial_update_civilian_hospital"),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Front Team Admin"
admin.site.site_title = "Front Team Portal"
admin.site.index_title = "Front Team Admin"

from django.contrib import admin
from threat.models import Threat


@admin.register(Threat)
class ThreatAdmin(admin.ModelAdmin):
    list_display = ('grid_x', 'grid_y', 'range',)

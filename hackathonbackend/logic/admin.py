from django.contrib import admin
from logic.models import TrainData


@admin.register(TrainData)
class TrainDataAdmin(admin.ModelAdmin):
    list_display = ("data", "target_category",)

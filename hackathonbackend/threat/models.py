from django.db import models
from neo4jintegration.views import update_node_value_method


class Threat(models.Model):
    grid_x = models.CharField("X position on the map", max_length=2, null=True, blank=True)
    grid_y = models.CharField("Y position on the map", max_length=2, null=True, blank=True)
    range = models.IntegerField("Range", null=True, blank=True)

    def __str__(self):
        return f"{self.grid_x}{self.grid_y}"

    def save(self, *args, **kwargs):
        super(Threat, self).save()
        update_node_value_method(f"{self.grid_x}{self.grid_y}", self.range)


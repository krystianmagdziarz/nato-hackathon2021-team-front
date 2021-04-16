from django.db.models.signals import pre_delete
from django.dispatch import receiver
from threat.models import Threat
from neo4jintegration.views import update_node_value_method


@receiver(pre_delete, sender=Threat)
def before_threat_remove(sender, instance, using, **kwargs):
    update_node_value_method(f"{instance.grid_x}{instance.grid_y}", 10)


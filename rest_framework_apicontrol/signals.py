import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import (
    Responsible,
    App,
    OrganizationalUnitType,
    OrganizationalUnit,
    LoggingGroup,
    LoggingEvent,
)


@receiver(pre_save, sender=Responsible)
@receiver(pre_save, sender=App)
@receiver(pre_save, sender=OrganizationalUnitType)
@receiver(pre_save, sender=OrganizationalUnit)
@receiver(pre_save, sender=LoggingGroup)
@receiver(pre_save, sender=LoggingEvent)
def update_updated_at_when_saving(sender, instance, **kwargs):
    instance.updated_at = datetime.datetime.now()

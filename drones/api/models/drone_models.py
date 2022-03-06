"""Drone model."""

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Utilities
from drones.utils.models import BaseModel
from drones.utils.constants import modelTypes, stateTypes, lg, idle


class Medication(BaseModel):
    """Medication model.

    The representation of a Medication for the bussines logic.
    """

    image = models.ImageField(
        upload_to="meds",
        help_text="The image of the med"
        )
    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The weight in gr of the med"
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )

    code = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    
    def __str__(self) -> str:
        """Return username."""
        return self.name



class Drone(BaseModel):
    """Drone model.

    The representation of a Drone for the bussines logic.
    """

    class modelChoices(models.TextChoices):
       Ligthweight= 'LI', _("Ligthweight")
       Middleweight= 'MI', _("Middleweight")
       Cruiseweight= 'CR', _("Cruiseweight")
       Heavyweight= 'HW', _('Heavyweight')
        
    model = models.CharField(
        max_length = 2,
        choices = modelChoices.choices,
        default = modelChoices.Ligthweight,
        help_text = "The model type of the drone"
    )

    class stateChoices(models.TextChoices):
       IDLE = 'ID',_("IDLE")
       LOADING = 'LA',_('LOADING')
       LOADED = 'LO',_('LOADED')
       DELIVERING = 'DI',_('DELIVERING')
       DELIVERED = 'DE',_('DELIVERED')
       RETURNING = 'RE',_('RETURNING')
        
    
    state = models.CharField(
        choices = stateChoices.choices,
        default = stateChoices.IDLE,
        max_length = 2,
        help_text = "The current state of the drone"
    )
    serial_number = models.CharField(
        max_length = 100,
        unique = True,
        help_text = "The serial number of the drones"
    )
    weight_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The weight limit that a dron can carry"
    )
    battery_capacity = models.IntegerField(
        default=100,
        help_text="The percent capacity of the battery"
    )

    medications = models.ManyToManyField(Medication, null=True)

    def __str__(self) -> str:
        """Return username."""
        return self.serial_number
    


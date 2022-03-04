"""Drone model."""

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Utilities
from drones.utils.models import BaseModel
from drones.utils.constants import modelTypes, stateTypes, lg, idle

class Drone(BaseModel):
    """Drone model.

    The representation of a Drone for the bussines logic.
    """

    model = models.PositiveSmallIntegerField(
        choices = modelTypes,
        default = lg,
        help_text = "The model type of the drone"
    )

    state = models.PositiveSmallIntegerField(
        choices = stateTypes,
        default = idle,
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

    
    medications=models.ForeignKey(
        "Medication",
        on_delete=models.SET_NULL,
        null=True,
        related_name="drones")
    def __str__(self) -> str:
        """Return username."""
        return self.serial_number
    

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

    drone_carrier = models.ForeignKey("Drone",
    on_delete=models.SET_NULL, null=True, related_name="medication")
    
    def __str__(self) -> str:
        """Return username."""
        return self.name

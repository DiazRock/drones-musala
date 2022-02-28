"""Drone model."""

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Utilities
from drones.utils.models import BaseModel

class Drone(BaseModel):
    """Drone model.

    The representation of a Drone for the bussines logic.
    """
    REQUIRED_FIELDS = [
        'drone_id',
        'serial_number', 
        'model', 
        'weight_limit',
        'battery_capacity',
        'state'
        ]

    class ModelType(models.TextChoices):
        Lightweight = 'L', _('Lightweight')
        Middleweight = 'M', _('Middleweight')
        Cruiseweight = 'C', _('Cruiseweight')
        Heavyweight = 'H', _('Heavyweight')
    
    class StateType(models.TextChoices):
        IDLE = 'I', _('IDLE')
        LOADING = 'LG', _('LOADING')
        LOADED = 'LE', _('LOADED')
        DELIVERING = 'DG', _('DELIVERING')
        DELIVERED = 'DE', _('DELIVERED')
        RETURNING = 'RG' , _('RETURNING')

    model = models.CharField(
        max_length = 2,
        choices = ModelType.choices,
        default = ModelType.Lightweight
    )

    state = models.CharField(
        max_length = 2,
        choices = StateType.choices,
        default = StateType.IDLE
    )
    drone_id = models.IntegerField(
        primary_key = True,
        help_text = "The id for drones in the database"
    )
    serial_number = models.CharField(
        max_length = 100,
        unique = True,
        help_text = "The serial number of the drones"
    )
    weight_limit = models.IntegerField(
        validators=[
            MaxValueValidator(500),
            MinValueValidator(1)
        ],
        help_text = "The weight limit that a dron can carry"
    )
    battery_capacity = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        help_text = "The percent capacity of the battery"
    )

    
    def __str__(self) -> str:
        """Return username."""
        return self.serial_number


    def get_current_state(self) -> StateType:
        """Get value from state""" 
        return self.StateType[self.state]

    def get_current_model(self) -> ModelType:
        """Get value from model""" 
        return self.ModelType[self.model]

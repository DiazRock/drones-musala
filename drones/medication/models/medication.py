"""Drone model."""

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Utilities
from drones.utils.models import BaseModel

# Model
from drones.drone_model.models import Drone

class Medication(BaseModel):
    """Medication model.

    The representation of a Medication for the bussines logic.
    """
    REQUIRED_FIELDS = [
        'name',
        'weight', 
        'code', 
        'image'
        ]

    image = models.ImageField(upload_to= "meds")
    weight = models.IntegerField(
        help_text = "The weight in gr of the med"
    )
    name = models.CharField(
        validators = [
            RegexValidator (
            regex = r'^[a-zA-Z0-9_-]+$',
            message = "Allowed only letters, numbers, '-', '_'"
        )
        ],
        max_length=100
    )

    code = models.CharField(
        validators = [
            RegexValidator (
            regex = r'^[A-Z0-9_]+$',
            message = "Allowed only letters, numbers, '-', '_'"
        )
        ],
        max_length=100
    )

    drone_carrier = models.ForeignKey(to= Drone, 
    on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        """Return username."""
        return self.name


""" Medication serializers """
# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers


# Models
from drones.medication.models import Medication



class MedicationModelSerializer(serializers.ModelSerializer):
    """Serializer for create a Med and store it in the db."""

    class Meta:
        """Meta class."""

        model = Medication
        fields = [
            'name',
            'weight', 
            'code', 
            'image'
        ]

    def validate(self, data):
        """Verify medication properties are correct."""
        code = data['code']
        regexValidator = RegexValidator (
            regex = r'^[A-Z0-9_]+$',
            message = "Allowed only letters, numbers, '-', '_'"
        )
        if not regexValidator.regex.fullmatch(code):
            raise serializers.ValidationError("Code not valid")
        
        return data

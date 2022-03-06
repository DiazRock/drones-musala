""" Medication serializer """

# Django
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers

# Models
from drones.api.models import Medication


class MedicationModelSerializer(
    serializers.ModelSerializer
    ):
    """Serializer for create a Medication and store it in the db."""

    class Meta:
        """Meta class."""

        model = Medication
        fields = [
            'id',
            'image', 
            'weight', 
            'name',
            'code'
        ]
    
    regex_name_validator= RegexValidator(
        regex='^[a-zA-Z0-9-_]+$',
        message='Medication name must be Alphanumeric',
        code='invalid_name'
    )

    regex_code_validator= RegexValidator(
        regex='^[A-Z0-9_]+$',
        message='Medication name must be Alphanumeric',
        code='invalid_name'
    )

    def validate(self, data):
        med_name = data['name']
        self.regex_name_validator(med_name)
        self.regex_code_validator(data['code'])
        return data
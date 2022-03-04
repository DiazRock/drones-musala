""" Drone_Model serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from drones.api.models import Drone


class DroneModelSerializer(serializers.ModelSerializer):
    """Serializer for create a Drone and store it in the db."""
    
    class Meta:
        """Meta class."""

        model = Drone
        fields = [
            'serial_number', 
            'model', 
            'weight_limit',
            'battery_capacity',
            'state'
        ]
    def create(self, validated_data):
        return super().create(validated_data)
    

""" Drone_Model serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from drones.drone_model.models import Drone


class DroneModelSerializer(serializers.ModelSerializer):
    """Serializer for create a Drone and store it in the db."""

    class Meta:
        """Meta class."""

        model = Drone
        fields = [
            'drone_id',
            'serial_number', 
            'model', 
            'weight_limit',
            'battery_capacity',
            'state'
        ]
    

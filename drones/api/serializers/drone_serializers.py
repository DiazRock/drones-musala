""" Drone_Model serializers """

# Django REST Framework
from rest_framework import serializers


# Models
from drones.api.models import Drone


class DroneModelSerializer(
    serializers.ModelSerializer):
    """Serializer for create a Drone and store it in the db."""
    
    class Meta:
        """Meta class."""
        model = Drone
        fields = [
            'id',
            'serial_number', 
            'model', 
            'weight_limit',
            'battery_capacity',
            'state'
        ]

    def validate(self, data):
        """ Validate no more drones than the fleet. """
        print(data)
        drone_count = Drone.objects.count()
        if drone_count > 10:
            return serializers.ValidationError('No more drones allowed')
        
        return data


    def update(self, instance, validated_data):
        print("Inside update")
        print(validated_data)
        print("**************")
        return instance


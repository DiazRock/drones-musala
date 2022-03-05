""" Drone_Model serializers """

# Django REST Framework
from drones.api.models.drone_models import Medication
from drones.utils import constants
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

        ret = super().validate(data)
        print("Data before ", data )
        drone_count = Drone.objects.count()
        if drone_count > 10:
            raise serializers.ValidationError('No more drones allowed')
        
        return ret


    def update(self, instance, validated_data):
        print("Inside update")
        print(validated_data)
        print("**************")
        instance.status = constants.ld
        medications = Medication.objects.filter(pk=validated_data['pk_med'])
        if self.weight_validation(medications.first(), instance):
            instance.medications.set(medications)

        else:
            raise serializers.ValidationError('Can\'t exced drone weight limit')
        

        return instance
    def weight_validation(self, medication, drone_instance):
        medications = drone_instance.medications.all()
        total_weight = sum([med.weight for med in medications.all()])
        return total_weight + medication.weight > drone_instance.weight_limit
            


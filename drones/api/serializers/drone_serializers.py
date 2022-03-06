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
    medications = serializers.PrimaryKeyRelatedField(queryset=Medication.objects.all(), required=False, many=True)
    class Meta:
        """Meta class."""
        model = Drone
        fields = [
            'id',
            'serial_number', 
            'model', 
            'weight_limit',
            'battery_capacity',
            'state', 
            'medications'
        ]
        

    def validate(self, data):
        """ Validate no more drones than the fleet. """
        ret = super().validate(data)
        pk = self.context['view'].kwargs['pk']
        instance = Drone.objects.get(pk=pk)
        drone_count = Drone.objects.count()
        if drone_count > 10 and not instance:
            raise serializers.ValidationError('No more drones allowed')
        
        return ret


    def update(self, instance, validated_data):
        if instance.battery_capacity < 25:
            raise serializers.ValidationError('Drone can\'t enter in LOADING status with battery capacity lower than 25%')
        instance.status = constants.ld
        medications = validated_data['medications']
        if self.weight_validation(medications, instance):
            instance.medications.set(medications)
        else:
            raise serializers.ValidationError('Can\'t exced drone weight limit')
        return instance

    def weight_validation(self, medications_list, drone_instance):
        medications = drone_instance.medications.all()
        total_weight = sum([med.weight for med in medications.all()])
        sum_weight = sum([med.weight for med in medications_list])
        return total_weight + sum_weight < drone_instance.weight_limit



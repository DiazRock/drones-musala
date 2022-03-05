from rest_framework import status, mixins, permissions
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drones.api.models import Drone, Medication
from drones.api.serializers import DroneModelSerializer, MedicationModelSerializer 
from rest_framework import viewsets


class DroneViewSet(viewsets.ModelViewSet):
    """
    Create a new drone.
    """
    allowed_methods= ['POST', 'PATCH', 'GET', 'PUT']
    serializer_class = DroneModelSerializer
    queryset= Drone.objects.all()
    #model= Drone

    # def get_queryset(self):
    #     """ Query set defined for drone """
    #     drone_id = self.kwargs.get('drone_id', False) 
    #     if drone_id:
    #         return self.queryset.filter(pk= drone_id)
    #     return Drone.objects.all()

    # def partial_update(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
 
    # def update(self, request, *args, **kwargs):
    #     return self.serializer_class.update(request.data)
        

class MedicationViewSet(viewsets.ModelViewSet):
    """
    Medication view set.
    """
    allowed_methods= ['POST', 'GET']
    serializer_class = MedicationModelSerializer
    queryset = Medication.objects.all() 
    
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drones.drone_model.models import Drone
from drones.drone_model.serializers import DroneModelSerializer 

class DroneView(
    mixins.CreateModelMixin
    ):
    """
    Create a new drone.
    """
    serializer_class = DroneModelSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

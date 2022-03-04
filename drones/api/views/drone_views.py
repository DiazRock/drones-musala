from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drones.api.models import Drone
from drones.api.serializers import DroneModelSerializer 
from rest_framework import viewsets


class DroneViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    """
    Create a new drone.
    """
    serializer_class = DroneModelSerializer
    queryset = Drone.objects.all() 

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

#  
       
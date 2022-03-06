from django.http.response import Http404
from rest_framework.decorators import action
from rest_framework.response import Response
from drones.api.models import Drone, Medication
from drones.api.serializers import DroneModelSerializer, MedicationModelSerializer 
from rest_framework import viewsets


class MedicationViewSet(viewsets.ModelViewSet):
    """
    Medication view set.
    """
    allowed_methods= ['POST', 'GET']
    serializer_class = MedicationModelSerializer
    queryset = Medication.objects.all() 
    

class DroneViewSet(viewsets.ModelViewSet):
    """
    Create a new drone.
    """
    allowed_methods= ['POST', 'PATCH', 'GET', 'PUT']
    serializer_class = DroneModelSerializer
    queryset= Drone.objects.all()


    @action(methods=['get'], detail=True,
            url_path='battery')
    def battery(self, request, *args, **kwargs):
        """Get the drone battery capacity """
        drone = Drone.objects.filter(pk= kwargs['pk']).first()
        if not drone:
            raise Http404
        serializer = self.get_serializer(drone)
        return Response({'battery_capacity': serializer.data['battery_capacity']})
        

    @action(methods=['patch'], detail=True,
            url_path='load')
    def load(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


    @action(methods=['get'], detail=True,
            url_path='medications')
    def medications(self, request, *args, **kwargs):
        """ Get the medications for a drone """
        drone = self.get_object()
        if not drone:
            raise Http404
        medications = drone.medications
        serializer = MedicationModelSerializer(medications, many=True)
        return Response(serializer.data)


    @action(methods=['get'], detail=False,
            url_path='availables')
    def availables(self, request, *args, **kwargs):
        """ Get drones availables for loading """
        available_drones = Drone.objects.filter(battery_capacity__gt= 25)
        serializer = self.get_serializer(available_drones, many=True)
        return Response(serializer.data)

    @action(methods=['get', 'patch'], detail=True,
            url_path='state')
    def state(self, request, *args, **kwargs):
        """ Get/Set drone state. 
        
        When you set drone in DELIVERED, the battery get 20% minus. 
        When you set drone in IDLE, the battery get 100% again.
        """
        current_drone = self.get_object()
        if not current_drone:
            raise Http404
        if request.method == 'GET':
            return Response({'state': current_drone.state})

        if request.method == 'PATCH':
            if request.data['state'] == 'IDLE':
                request.data['battery_capacity'] = 100
            if request.data['state'] == 'DELIVERED':
                request.data['battery_capacity'] -= 20
            serializer = self.get_serializer(
                current_drone,
                data = request.data,
                partial = True
            )
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
    
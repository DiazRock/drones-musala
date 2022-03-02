""" Medication Views """

# Django rest framework
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drones.medication.models import Medication
from drones.medication.serializers import MedicationModelSerializer 

class MedicationViewSet(
    mixins.CreateModelMixin
    ):
    """
    Create a new medication.
    """
    serializer_class = MedicationModelSerializer
    
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)

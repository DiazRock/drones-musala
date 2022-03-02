""" Drone app urls """

# Django
from django.urls import path

# Django Rest Framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from drones.drone_model.views import DroneView

urlpatterns = [
    path('drone/', DroneView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
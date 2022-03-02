"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import medication as medication_views

router = DefaultRouter()
router.register(r'medication', 
    medication_views.MedicationViewSet, 
    basename='medication')

urlpatterns = [
    path('', include(router.urls))
]

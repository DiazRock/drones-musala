"""api URLs."""

# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework.routers import SimpleRouter

# Views
from drones.api.views import drone_views


router = SimpleRouter()
router.register(r'drone', drone_views.DroneViewSet, basename='drone')
router.register(r'medication', drone_views.MedicationViewSet, basename='medication')


urlpatterns = [
    path('', include(router.urls))
]

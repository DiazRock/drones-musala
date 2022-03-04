"""api URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from drones.api.views import drone_views

router = DefaultRouter()
router.register(r'drone', drone_views.DroneViewSet, basename='drone')

#import ipdb; ipdb.set_trace()

urlpatterns = [
    path('', include(router.urls))
]

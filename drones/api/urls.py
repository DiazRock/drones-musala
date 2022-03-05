"""api URLs."""

# Django
from django.urls import include, path

# Views
from drones.api.views import drone_views

# Utils
from drones.utils.router import BulkRouter

router = BulkRouter()
router.register(r'drone', drone_views.DroneViewSet, basename='drone_views')
router.register('drone/available', drone_views.DroneViewSet, basename='drone_views')
router.register(r'drone/(?P<drone_id>\d+)/load', drone_views.DroneViewSet, basename='drone_views')
router.register(r'medication', drone_views.DroneViewSet, basename='drone_views')

#import ipdb; ipdb.set_trace()

urlpatterns = [
    path('', include(router.urls))
]

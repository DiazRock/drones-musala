# Django REST Framework
from rest_framework.routers import DefaultRouter, SimpleRouter

import copy

class BulkRouter(DefaultRouter):
    """
    Map http methods to actions defined on the bulk mixins.
    """
    routes = copy.deepcopy(SimpleRouter.routes)
    routes[0].mapping.update({
        'put': 'update',
        'patch': 'partial_update'
    })


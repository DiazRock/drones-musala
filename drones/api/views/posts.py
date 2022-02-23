"""Post views."""

# Django Rest Framework
from rest_framework import viewsets

# Own
from drones.api.serializers import PostModelSerializer
from drones.api.models import Post

class PostViewSet(viewsets.ModelViewSet):
    """ Post view set
        Handle all CRUD requests
    """

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    
       
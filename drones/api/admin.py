"""Api admin."""

# Django
from django.contrib import admin

# Models
from drones.api.models import Drone, Medication

@admin.register(Drone, Medication)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('id','created', 'modified')
    search_fields = ('created',)
    list_filter = ('created',)

 
"""Celery tasks."""

# Django
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone

#Model
from drones.api.models import Drone

# Celery
from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger


# Utilities
from datetime import timedelta


logger = get_task_logger(__name__)


@periodic_task(
    run_every=(timedelta(seconds=10)),
    name="check drone battery capacity for the drone fleet",
    ignore_result=True
)
def check_available_drones():
    """Check the battery capacity of the drones and send the info to a log file."""
    drones = Drone.objects.all()
    logger.info("Checking battery capacity of the drone fleet")
    a = [x for x in drones.values()]
    logger.info('\n'.join('Drone:{2}---{0}:{1}'.format(x['serial_number'], x['battery_capacity'], x['id']) for x in a))

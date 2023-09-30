from django.apps import AppConfig
from django.db.models.signals import post_save


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from robots.models import Robot
        from . import signals
        post_save.connect(signals.robot_saver, sender=Robot)

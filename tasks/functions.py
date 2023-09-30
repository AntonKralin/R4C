from django.utils import timezone
import json

from .exceptions import ValidJSON, DublicateData
from robots.models import Robot
from .classess import RobotData, OrderData


def parse_json(data: json) -> Robot:
    try:
        r_data = RobotData(**data)
        robot = Robot()
        robot.model = r_data.model
        robot.version = r_data.version
        robot.serial = '-'.join([robot.model, robot.version])
        aware_datetime = timezone.make_aware(r_data.created,
                                             timezone.get_current_timezone())
        robot.created = aware_datetime
        return robot
    except ValueError:
        raise ValidJSON('Wrong JSON data')


def parse_order(data: json) -> OrderData:
    try:
        o_data = OrderData(**data)
        return o_data
    except ValueError:
        raise ValidJSON('Wrong JSON data')


def save_robot(robot: Robot):
    dupl = Robot.objects.filter(model=robot.model, version=robot.version,
                                created=robot.created).exists()
    if dupl:
        raise DublicateData('The same robot', robot)
    else:
        robot.save()

from robots.models import Robot
from customers.models import Customer
from orders.models import Order


def create_order(data) -> bool:
    r_count = Robot.objects.filter(serial=data.serial)
    if len(r_count) > 0:
        robot = r_count[0]
        robot.delete()
        return True
    customer = Customer.objects.get_or_create(email=data.email)
    customer.save()
    order = Order(customer=customer, robot_serial=data.serial)
    order.save()
    return False

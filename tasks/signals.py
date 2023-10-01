from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

from robots.models import Robot
from orders.models import Order


@receiver(post_save, sender=Robot)
def robot_saver(sender, instance, **kwargs):
    orders = Order.objects.filter(robot_serial=instance.serial)
    if len(orders) > 0:
        order = orders[0]
        customer = order.customer
        text = f"""
        Добрый день!
Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами
        """
        send_mail('Order', text, 'robot@main.company', [customer.email])
        customer.delete()
        instance.delete()

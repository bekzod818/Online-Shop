from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f"Dear {order.first_name} {order.last_name},\n\nYou have successfully placed an order.\nYour order ID is {order.id}."
    mail_sent = send_mail(subject, message, 'bekzod030900@gmail.com', [order.email])

    return mail_sent

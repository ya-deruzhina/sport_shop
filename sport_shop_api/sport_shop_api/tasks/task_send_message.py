from sport_shop_api.celery import app
from apps.shop.models import *
from django.core.mail import send_mail

@app.task()
def send_message_task (order_number):
    send_mail(
                f'Order {order_number}',
                'Thank you for your order',
                'moya_powta@list.ru',
                ["moya_powta@list.ru"],
            )
    print('Message Sent')
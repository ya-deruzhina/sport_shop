from sport_shop_api.tasks.task_send_message import *
from sport_shop_api.celery import app as celery_app

__all__ = ('celery_app',)

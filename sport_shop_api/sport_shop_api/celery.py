# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import dotenv
from pathlib import Path

path_to_env = Path(__file__).parents[1].joinpath(".env")

dotenv.load_dotenv(dotenv_path=path_to_env)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'development')

app = Celery('sport_shop_api')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = os.getenv('CELERY_BROKER_URL')



app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print ('task')

debug_task.delay()
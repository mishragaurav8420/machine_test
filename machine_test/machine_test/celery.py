import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTING_MODULE','machine_test.settings')
app=Celery('machine_test')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()
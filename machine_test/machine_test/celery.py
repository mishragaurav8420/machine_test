import os
import speedtest
from celery import Celery
from celery.schedules import crontab
from celery import shared_task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'machine_test.settings')
app = Celery('machine_test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@shared_task
def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    print(f"Download Speed: {download_speed} Mbps")
    print(f"Upload Speed: {upload_speed} Mbps")

# Configure the Celery beat schedule
app.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'machine_test.tasks.check_internet_speed',  # Update the task path
        'schedule': crontab(minute='*/1'),
    },
}

# Start the Celery beat scheduler
app.conf.timezone = 'UTC'
app.conf.enable_utc = True

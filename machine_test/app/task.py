from celery import shared_task
@shared_task
def my_task(data):
    result=data*2
    return result
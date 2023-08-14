from celery import shared_task
from time import sleep

@shared_task(bind=True)
def test_task(self, x):
    for i in range(x):
        sleep(3)
    return 'Task done'

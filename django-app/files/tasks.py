from celery import shared_task
from time import sleep
from django.http import HttpResponse
import csv

@shared_task(bind=True)
def generate_csv(self, user):
    pass
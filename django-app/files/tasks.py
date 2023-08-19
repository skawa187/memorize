from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from zoneinfo import ZoneInfo
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from memo.models import Memo
import os, csv

logger = get_task_logger(__name__)

@shared_task(bind=True)
def generate_csv(self, id, uuid):
    fs = FileSystemStorage()
    file_list = fs.listdir(fs.base_location)[1]
    csvfile_name = datetime.now().strftime('%Y-%m-%d_%H-%M')
    user_dir = os.path.join(fs.base_location, str(uuid)[:13])
    local_tz = 'Europe/Warsaw'
    memo_q = Memo.objects.filter(user_id=id)

    if not os.path.exists(user_dir): # Create the user dir
        os.makedirs(user_dir)
    if memo_q:
        path = os.path.join(user_dir, csvfile_name)
        with open(path, 'w', newline='') as csv_file:  # Open a file to write the query results
            djfile = File(csv_file)
            writer = csv.writer(djfile, dialect='excel')
            writer.writerow([*memo_q.values()[0].keys()][2:]) # First (header) row
            for memo in memo_q.values():
                values = [*memo.values()][2:]
                for idx, i in enumerate(values):    # Convert datetime objects
                    if type(i) == datetime:
                        i = i.astimezone(ZoneInfo(local_tz))
                        values[idx] = i.strftime('%d/%m/%Y %H:%M')
                writer.writerow(values) # Value rows

    logger.info('File list {}'.format(file_list))
    logger.info('File name {}'.format(csvfile_name))
    return 'Task result {}, {}, uuid: {}'.format(csvfile_name, file_list, uuid)
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from zoneinfo import ZoneInfo
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from memo.models import Memo
import os, csv

logger = get_task_logger(__name__)

@shared_task(bind=True)
def generate_csv(self, id, uuid):
    fs = FileSystemStorage()
    file_list = fs.listdir(fs.base_location)[1]
    csvfile_name = '.'.join((datetime.now().strftime('%Y-%m-%d_%H-%M'), 'csv'))
    user_dir = os.path.join(fs.base_location, str(uuid)[:13])
    local_tz = 'Europe/Warsaw'
    memo_q = Memo.objects.select_related('category').filter(user_id=id)

    if not os.path.exists(user_dir): # Create the user dir
        os.makedirs(user_dir)
    if memo_q:
        path = os.path.join(user_dir, csvfile_name)
        with open(path, 'w', newline='') as csv_file:  # Open a file to write the query results
            djfile = File(csv_file)
            writer = csv.writer(djfile, dialect='excel')
            writer.writerow([*memo_q.values()[0].keys()][2:]) # First (header) row
            for i in range(memo_q.count()):
                values_dict = memo_q.values()[i]
                [values_dict.pop(key) for key in ['id', 'user_id']]
                for k, v in values_dict.items():    
                    if isinstance(v, datetime):  # Convert datetime objects
                        v = v.astimezone(ZoneInfo(local_tz))
                        values_dict[k] = v.strftime('%d/%m/%Y %H:%M')
                    elif type(k) == str and k.endswith('_id'):
                        expr = 'memo_q[{}].{}.name'.format(i, k.rstrip('_id'))
                        values_dict[k] = eval(expr)    # Get category name from a related model                 
                writer.writerow([*values_dict.values()])     # Value rows

    logger.info('File list {}'.format(file_list))
    logger.info('File name {}'.format(csvfile_name))
    return 'Task result {}, {}, uuid: {}'.format(csvfile_name, file_list, uuid)
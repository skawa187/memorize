from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from .tasks import generate_csv
from .celery import debug_task


class UserFilesView(TemplateView):
    from django.core.files.storage import FileSystemStorage
    template_name = 'files/file-list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        fs = self.FileSystemStorage()
        file_list = fs.listdir(fs.base_location)[1]
        ctx['file_list'] = file_list
        ctx['base_url'] = fs.base_url
        print('CTX {}'.format(ctx))
        return ctx

def generate_csv_task(request):
    """
    Runs a task to create a new csv file for this user
    """
    task = generate_csv.delay(request.user.id, request.user.uuid)
    messages.add_message(request, messages.SUCCESS, 'Added a new csv file request, ID: {}'.format(task))

    return redirect('file-list')
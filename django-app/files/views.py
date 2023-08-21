from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from os import path

from .tasks import generate_csv

class UserFilesView(LoginRequiredMixin, TemplateView):
    from django.core.files.storage import FileSystemStorage
    template_name = 'files/file-list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        fs = self.FileSystemStorage()
        user_dir = str(self.request.user.uuid)[:13]
        file_list = fs.listdir(user_dir)[1]
        file_urls = [f'{fs.base_url}{user_dir}/{file}' for file in file_list]
        file_dict = { file_list[i]: file_urls[i] for i in range(len(file_list))}
        ctx['user_files'] = file_dict
        ctx['user_dir'] = user_dir
        print('CTX {}'.format(ctx))
        return ctx

def generate_csv_task(request):
    """
    Runs a task to create a new csv file for this user
    """
    task = generate_csv.delay(request.user.id, request.user.uuid)
    messages.add_message(request, messages.SUCCESS, 'Added a new csv file request, ID: {}'.format(task))

    return redirect('file-list')
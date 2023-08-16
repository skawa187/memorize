from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse


class UserFilesView(TemplateView):
    from django.core.files.storage import FileSystemStorage
    template_name = 'files/file-list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        fs = self.FileSystemStorage()
        file_list = fs.listdir(fs.base_location)[1]
        ctx['file_list'] = file_list
        ctx['base_url'] = fs.base_url
        print(ctx)
        return ctx

def generate_csv_task(request):
    uuid = request.user.uuid
    print(str(uuid)[:8])
    response = HttpResponse('Generating the new csv file')
    return response
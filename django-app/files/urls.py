from django.urls import path
from .views import UserFilesView, generate_csv_task

urlpatterns = [
    path('', UserFilesView.as_view(), name = 'file-list'),
    path('gen/', generate_csv_task, name = 'file-gen'),
]
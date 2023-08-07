from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Memo

class MemoList(ListView):
    model = Memo
    template_name = 'memo/memos.html'
    context_object_name = 'memo_list'

class MemoDetail(DetailView):
    model = Memo
    template_name = 'memo/memo-detail.html'
    context_object_name = 'memo'

class MemoCreate(CreateView):
    model = Memo
    template_name = 'memo/memo-create.html'
    fields = '__all__'
    success_url = reverse_lazy('memo-list')

class MemoUpdate(UpdateView):
    model = Memo
    template_name = 'memo/memo-create.html'
    fields = '__all__'
    success_url = reverse_lazy('memo-list')

class MemoDelete(DeleteView):
    model = Memo
    template_name = 'memo/memo-delete.html'
    context_object_name = 'memo'
    success_url = reverse_lazy('memo-list')

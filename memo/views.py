from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Memo

class MemoList(ListView):
    model = Memo
    template_name = 'memo/memos.html'

class MemoDetail(DetailView):
    model = Memo
    template_name = 'memo/memo-detail.html'
    context_object_name = 'memo'
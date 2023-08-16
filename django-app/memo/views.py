from typing import Any, Dict
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib.auth import login, get_user_model
from .models import Memo
from .forms import CustomRegisterForm

class SignupView(FormView):
    form_class = CustomRegisterForm
    User = get_user_model()
    template_name = 'memo/signup.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        messages.add_message(self.request, messages.SUCCESS, 'Successfully created a new user!')
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)

class UserLoginView(LoginView):
    fields = '__all__'
    template_name = 'memo/login.html'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('memo-list')

class MemoList(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memo/memos.html'
    context_object_name = 'memo_list'

    def get_queryset(self):
        return Memo.objects.filter(user=self.request.user)

class MemoDetail(LoginRequiredMixin, DetailView):
    model = Memo
    template_name = 'memo/memo-detail.html'
    context_object_name = 'memo'

class MemoCreate(LoginRequiredMixin, CreateView):
    model = Memo
    template_name = 'memo/memo-create.html'
    fields = ['title', 'body', 'importance', 'category',]
    success_url = reverse_lazy('memo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MemoCreate, self).form_valid(form)

class MemoUpdate(LoginRequiredMixin, UpdateView):
    model = Memo
    template_name = 'memo/memo-create.html'
    fields = ['title', 'body', 'importance', 'category',]
    success_url = reverse_lazy('memo-list')

class MemoDelete(LoginRequiredMixin, DeleteView):
    model = Memo
    template_name = 'memo/memo-delete.html'
    context_object_name = 'memo'
    success_url = reverse_lazy('memo-list')


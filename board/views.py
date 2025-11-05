from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Task

# Create your views here.


class HomeView(TemplateView):
    template_name = 'board/index.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'board/authorized.html'
    login_url = '/admin'
    all_task = Task.objects.all()
    extra_context = {'list_task': all_task}

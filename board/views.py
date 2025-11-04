from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

from . models import Task

# Create your views here.


def board(request):
    return render(request, 'board/Index.html', {'today': datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    all_task = Task.objects.all()
    return render(request, 'board/authorized.html', {'list_task': all_task})

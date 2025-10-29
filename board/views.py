from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def board(request):
    return render(request, 'board/Index.html', {'today': datetime.today()})

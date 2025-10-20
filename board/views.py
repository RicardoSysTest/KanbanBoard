from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def board(request):
    return HttpResponse('Hello World')

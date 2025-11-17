from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = 'smart/notes'


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

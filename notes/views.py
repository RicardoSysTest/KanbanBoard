from django.shortcuts import render
from .models import Notes

# Create your views here.


def list(request):

    # Get all notes store in our DB
    all_notes = Notes.objects.all()

    # Return the render or the template note_list.html
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

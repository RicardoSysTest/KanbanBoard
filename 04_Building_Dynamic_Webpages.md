## Buildin Dinamic Webpages



## Creating 
Now that we have our notes, let's create a new view to display them in the same way we created the other one. From notes app open  `views.py` start with importing the models and import notes. Okay, now let's create a function call list that receives a request and then a variable, all_notes that stores all the notes that we have in our database. Now, let's return the render function again, request a template that we're going to create a little bit later, notes/notes_list.html, and now the brackets with notes are equal to all_notes
```py
    from django.shortcuts import render
    from .models import Notes

    def list(request):
        all_notes = Notes.objects.all()
        return render(request, 'notes/notes_list.html',{'notes':all_notes})


    # Create your views here.  
```
This is not much different from what we did in the other view, except for one thing, we are querying for all notes and sending them to the template. This way, when the template is rendered, all the information coming directly from the database will be available. Before we jump to the template, let's organize URLs. 

So let's create a new URLs file here in the notes app and that's going to have the same format. So from django.urls import path. Then let's import the views here, and then the urlpatterns that has a list. Then here, the path, our endpoint's going to call notes because that's the list of notes. Then views.list, which is the function we just created. 
```py
    from django.urls import include, path
    from . import views

    urlpatterns = [
        path('notes', views.list),
    ]
```
The last thing is that we have to add this on the urls.py file on smart notes. So let's add comma here, then path. Let's add smart here, and then include notes.urls.
```py
from django.contrib import admin
from django.urls import include, path

from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("board.urls")),
    path('smart/', include("notes.urls")),
]

```
All the URLs that we are adding on notes.urls will be added after the smart. So smart's going to be a part of that endpoint. This is a really nice way of organizing our project. Okay, almost there. Now we need to create the template folder. So notes, new folder, templates, then a new folder, notes, and now we can add our template. Notes_list.html. 


Okay, now we can create our template. So let's start by html and h1, these are the notes.  And I will start to use the powers of DTL. Bear with me just a little bit. So let's start with ul, and then curly brackets, two percentages, and in the middle, for note in notes. Okay, so in here we're going to add a line item, {{note.title}} close the curly brackets, and now we need to do curly brackets, percentage, percentage, and in the middle it's going to have an endfor.
```html
    <html>
    <h1>These are the notes</h1>
        <ul>
            {% for note in notes %}
            <li>{{note.title}}</li>
            {% endfor %}
        </ul>
    </html>
```
Okay, what's happening here? Everything that is between curly brackets is the django template language logic. Here, we're opening a list tag, ul, and then saying that for each note we receive in the template, DTL should create a list item, the li. Notice that commands such as the loop happen between curly brackets and percentages, while things that should be rendered by the template are between double brackets. So let's save this, then run this, runserver and open it. Okay, now we can see that we have a smart here. Then let's try this smart. We're going to have the notes and here are the notes. There it is, a webpage that is dynamically getting data from the database and adding it to the HTML. If we right click here and inspect the page, we'll see here that we actually have two line items. That's because we have only two nodes on the database. If we had many more, many more would be created. How easy was that? I encourage you now to go and create more notes, either via the shell or the admin and see what happens here.
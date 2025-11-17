## Django Forms

## Create a webpage
Whenever we're building a system, there's a couple of common operations that we should support for every model we create. These are: 
* Create 
* Read 
* Update
* Delete
 
Those are the CRUD operations. These are the minimal operations that a system should typically support. So far regarding the notes model, we implemented the retrieve method by having an endpoint to get the details of a particular note. To fully support the notes model, we need to handle all the other three operations as well. Now we're going to learn how to implement a create method. 

Let's go back to notes, views.py, and in here, let's import, well, I hope you guess it, CreateView. Once we have this, we can actually start our new class. So class NotesCreateView that inherits from CreateView. 
```py
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes

# Create your views here.


class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

```

And we're going to need three things here. So model = Notes, fields which is going to be ['title', 'text']. And finally, a success_url. That is going to be the '/smart/notes' which is our list endpoint. Let's understand what's going on here. First the model. So the endpoint understands what is regarding to. Then the fields will be the attributes from the model that we allow a user to fill. Since we don't need to pass a created add field, we just define it as title and text. Finally, we want to redirect the user to the list of existing notes so they can see the note they just created. This is the success_url attribute here. And that's it. That's all we need to do in this class. 
```py
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes

# Create your views here.
class NotesCreateView(CreateView):
    model =  Notes
    field = ['title', 'text']
    success_url = '/smart/notes'

class NoteListView(ListView):
    model = Notes
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

```

Now we can add the endpoint to the urls.py file, the same way we did to every other endpoint so far. So in here, let's add path 'notes/new', and then we can call views.NotesCreateView.as_view(). And let's not forget to pass a name to it. So "notes.new", and a comma here. 
```py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
    path('notes/new',views.NotesCreateView.as_view(), name="notes.new"),
]

```

Okay, so the last thing that's missing is the template. So let's create it. Let's call it notes_form.html. Okay, so let's use the default template. So extends 'base.html' and then the block content, and finally, the endblock. Okay, so now we can start. To send information back to the server, we'll need a form tag from the HTML. So let's add this here. Okay, so in the form we can do action is equal to, we're going to use the method url and then notes.new, which is the endpoint we just created. And also the method here needs to be POST because we're sending information back to the server. Okay, so now what we need is to allow a user to pass back the information we defined on our endpoint, title and text. How do we do that? Well, this can't be more simple. In here, we can do double curly brackets then form, and that's it. Want to see what happens here? Let's go back to the browser and try out our new endpoint.
```html
{% extends 'base.html'%}

{%block content%}
<form action="{url 'notes.new'}" method='POST'>
    {{ form }}
</form>
{% endblock %}
```

 So in here we can open the inspector element. And you can see here that in the body we have a form, and the form is actually passed down to the HTML as two label tags, and one input tag and one text area. This is because Django already knows which type of data each attribute expects. Thus it creates an appropriate HTML tag to receive it. Well, we're still missing the submit button, so let's add that. So in here, let's add button type="submit." The class is going to be ="btn btn-primary." Let's add some vertical alignment, Submit. That's it. 
 ```html
 {% extends 'base.html'%} {%block content%}
<form action="{url 'notes.new'}" method="POST">
  {{ form }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>
{% endblock %}
 ```
 
 
 Now we have everything we need in place. That is basically all we have to do to have an endpoint to create a new note.

## Understanding how Django Handles Security in POSTs
We did everything we needed to do to implement the create endpoint. But if you try to create a new note, you'll notice that it will actually return a 403 error, meaning that we are forbidden to do this action. Well, we're actually missing one less thing to our form. So if you go here, we can add {%, and then a csrf_token, and that's it. 
```html
{% extends 'base.html'%} {%block content%}
<form action="{url 'notes.new'}" method="POST">
  {% csrf_token %} {{ form }}
  <button type="submit" class="btn btn-primary my-5">Submit</button>
</form>
{% endblock %}

```

So let's try again. We can go back. Refresh this page. So this is a new note. It worked. Let's submit. And yes, indeed it works. You're probably wondering, what is this magic that was missing? This is a CSRF token. That stands for Cross-Site Requests Forgery. What happens here is that every time a browser requests a webpage that has a form, Django will send a unique token to that browser. This token will be securely kept and no other website can access it. When the user sends back a form, it'll also send back the token, allowing Django to know that this request is coming from a legit user. Django will then process the request and return the appropriate response. However, if for some reason a third party have access to the user credentials, when they try to make the request from another browser, they won't have the token. So Django understand that this request is coming from an unreliable source and will not process the request, thus, preventing this type of attack. As you can see, this is an additional layer of security that Django is adding to your website with just a small line of code. Beyond the numerous features that allow you to speed up the process of creating a website, these security features are a big part of why developers choose Django to work with.

## Django forms: Powerfil validation with miinimal Work


## Django forms are useful for layout as well


## Codespaces error and the solution
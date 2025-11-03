## Database with Django


## Introduction to ORMS
So far, you've gotten familiarized with the user models, which were completely defined by Django. Now, it's time to understand how to create your own models and how the structure of creating models work. Django uses an object-relational mapping system or ORM to handle database communication and changes. 
![alt text](image-1.png)

What you need is to write class models that will then be transformed by migrations into database tables. Each class, known as a model, is a database table, and each class attribute is a column. The way we transform a model into a database table is by the creation of migrations. Migrations will have the step-by-step transformation that a database must do to apply the changes made in the code. You've seen that we use the command Migrate to apply migrations to a database. Similarly, we can use the command MakeMigrations to create migrations based on the current code. The process of using a class, defining a model, creating a migration, and applying the migration and the changes to the database is the ORM's job, and Django's ORM is known for being 
one of the best ORMs for Python and SQL databases.


## Creating your first Model
Learn how to create a new model using Django ORM. 

1. Let's create a new app specifically for our notes. 
```bash
 django-admin startapp notes
```

2. We have to go to the settings and make sure that our new app is added in the INSTALLED_APPS variable.
```py
  # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'board',
    'notes'
] 
```
3. Okay, now we can go back to this new app (`notes`) and open the `models.py` file. Here is the file where we can create the models that we'll use in this app. So let's create a new class called Notes that we'll inherit from models.Model.
```py
   from django.db import models

    # Create your models here.
    class Nodes(models.Model):
        
```

This way, Django knows that this is a model that will have effect on the database, et cetera.

4. It's time for us to think what attributes we want in our note. Well, first we can add a title. A title is a short text, so we can use the type CharField, which is a limited text field. CharField has a parameter called max_length, and we should set it to a value. Let's say 200. This means that our title can't be over 200 characters. We also need the note itself. And the note shouldn't have a limit. So instead of using CharField, we can use the type TextField. As you can see, TextField doesn't require a max length, differently from CharField. We also want to know when this note was created. So we can add a field call created that is going to be a DateTimeField. Because we don't really want to worry about this field being correctly populated, we can add a perimeter called auto_now_add equals to True. This means that every time a note is created, this field will be correctly populated with the time that this note was created. So we don't really have to worry about it. There, our notes model is done. Every note we create will have at least a title, a text, and a date. 
```py
   from django.db import models

    # Create your models here.
    class Nodes(models.Model):
        title = models.ChartField(max_length=200)
        text = models.TexField()
        created = models.DateTimeField(auto_now_add_True)
```
5. Now we need to create migrations.
```bash
   python manage.py makemigrations
``` 
There is a new folder called migrations, and inside of it, there's a new file called 001_intial. Every first migration of an app will be named like this. If you open this, you can see that this is just a list of operations that instructs the database what needs to be done. So far, we haven't changed anything in the database. We just created the set of instructions. So everything continues as it is. 
6. Then we need to apply the migrations so we can run:
```bash
    py manage.py migrate
``` 
The changes were applied to the database and we have a shiny new table.

## Using Adming for data creation and manipulation
We've already created a table for notes, but if you're curious enough to go to the Django admin interface, you'll notice that nothing really changed. Why is that? The same way we didn't have to create the user model, it was just there, we didn't have to configure it to appear on the Django interface. When we are creating a new model, we need to do it ourselves. So, let's go back to the notes app and open a file called `admin.py` 

This is where we're going to add which models can be displayed, and thus modified, via the Django admin interface. First, let's create a class and call it NotesAdmin. This class should inherit from admin.ModelAdmin.  Let's add pass here because we don't want any additional configuration on this admin model
```py
# Fomr this folder import models
from . import models

from django.contrib import admin

# Register your models here.
class NotesAdmin():
    pass
```
Now, what we need to do is import from this folder, let's import models, and on the bottom of the file, we're going to register that that model is attached to this admin model. So, let's write admin.site.register, then models.Notes, and NotesAdmin. Okay, that's it. Let's go back to the admin and refresh it. 
```py
# Fomr this folder import models
from . import models

from django.contrib import admin

# Register your models here.
class NotesAdmin():
    pass


admin.site.register(models.Notes, NotesAdmin)
```
Now we can see that the notes model is available on the admin interface. Let's use the add button here to create a new note. 
![alt text](image-2.png)

Let's title My first Note, and then Django is so Amazing! Let's save this. Okay, we have our first note created. One thing that isn't really nice is that it is listed as this Notes object 1. 
![alt text](image-3.png)
This is fine for now, but if we have a long list of notes, how can we tell which one is which? Let's go back to the admin class. Instead of pass here, we can pass list display, which is going to be a tuple. And let's pass title here. 
```py
# Fomr this folder import models
from . import models

from django.contrib import admin

# Register your models here.
class NotesAdmin():
    list_display = ('title', )


admin.site.register(models.Notes, NotesAdmin)
```
Let's save this. It restarted. And now if we refresh here, there, instead of having this ugly name, we have the title of the note being displayed here. 
![alt text](image-4.png)
The default configuration of admin also allows that all fields can be changed by all users. However, we can edit the admin model class and start adding some specialized logic. We can remove some fields from being edited. We can allow only staff users to write notes. There's a lot we can do. The sky's the limit. Django admin is highly configurable.

## Using Django shell for creating and quering data.

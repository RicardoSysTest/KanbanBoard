# Kanban Board with Django

1. To start the Virtual Enviroment execute the following command: 
```bash
    ./venv/Scripts/activate
```

2. Install django with the following command
```bash
    pip install django
```

3.Create Django Project with the following command:
```bash
    django-admin startproject kanban .
``` 

4. Ensure that everything starting the server
```bash
   py manage.py runserver
```

5. Create Django App with command:
```bash
    py manage.py startapp board
```

6. Install application in the setting folder from the project kanban. 
```py
   INSTALLED_APPS =[
    ...
    #apps
    'board',
   ]
```

7. Create the first view of the app. Go the boar folder and open the view file.
```py
    from django.shortcuts import render
    from django.http import HttpResponse

    def board(request):
        return HttpResponse('Hello, wolrd')
```

8. Then go back to the ulrs file from the main project and update the file with:
```py
from django.urls import path

from board import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('home/',views.board),
]
```

9. Then we need to confirm that everything is working with the command
```py
   py manage.py runserver
```
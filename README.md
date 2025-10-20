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
    board,
   ]
```
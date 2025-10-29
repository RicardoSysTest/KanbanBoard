
# 02 User Manager from Django Framwework

## Django Admin Easly Visualizing and Creating Data
By default django will have and entire authentication system ready to go. The only thing we need to do is to make sure our database is properly configure. Django knows if the database is behind the system changes trough a couple of files colled migrations. By default Django already has the migrations for the authtnetication system ready, so what you need to do is apply them to the database, so what you need to do is apply them to the database with the command migrate:
```bash
   py managege.py migrate
```

Since now out database is up to speed with Django, what we need is to create a superuser that will have all the power that it can in this Django project. We do this by running the command `createsuperuser`.

## Migrations: Making Database Changes Easy
Create user with the Django Addmin is a safe way to handle multiple users.


## User authentication in two simples steps
You learn that Django comes with a power authentication system already to be used. 

1. Come back to the templates folder and go to the sub-folder home. Here create a new file call `authorized.html`
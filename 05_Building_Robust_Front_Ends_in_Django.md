## Robus Front End with Django

## Static Files in Django
It is time to think about our project's front end. Our templates are too simple with just HTML on them, so let's add some colors! The first thing we need to do is create a folder where we're going to store all the static files, such as the CSS and JavaScript files, images, videos, et cetera. So let's go here, and create new folder `static`. Now we need to tell Django that this is the folder it needs to look into when searching for static files. To do that, let's go to the `smartnotes\settings.py`. Then in here, we can scroll down a little bit, and we're going to see here that there is a static URL already. 
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
Now we're also going to add static files, underline, dirs. This should be a list. And in here we're going to say, base dir, slash, static, which will lead Django to the folder we just created. 
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

Okay, now we can go back to the static, and create a new folder just for the CSS files, and one CSS file, let's call it style `static/css/style.css` . Okay, so in here we can create a simple CSS file. 

Let's create a class called, note-li, color equals red.   
```css
.note-li{
    color: red;
}
```
What we need to do now is make sure that our template, and Django per se, recognizes this file. So let's go to the notes, and let's try the `notes_list.html`. The first thing we need to do is actually tell Django that this HTML is going to use the static files. So let's go curly brackets, percentages, and load static (`{% load static %}`). Okay, now what we need here is to add a CSS file as we would in any HTML file. So let's create a head, then a link. So the rel is going to be stylesheet. The type is going to be text, CSS, and on the href, we're going to use the Django template language to add our URL. So let's call static, then CSS style dot CSS. That's it. That's all we need to do to have the CSS being rendered on this file. So let's go here to tag `li`, and add the class, which is going to be our class name `<li class="note-li"></li>`, let's save it and try it.
```html
{% load static %}
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css'%}"/>
  </head>
  <h1>These are the notes</h1>
  <ul>
    {% for note in notes %}
    <li class="note-li">{{note.title}}</li>
    {% endfor %}
  </ul>
</html>

```
  I'm going to refresh this. And there you go. Now the notes are red because the CSS is being rendered and used in this file. If we open the inspector here, we can see here that the head is appearing. We have the href here being correctly rendered, and then each note here has the class that has the attribute of color red. If you hover this href, you'll notice that this is actually a link. So let's go here. Let's copy this, and then we can replace it here. And there you go. As you can see here, this is the file we just created. So actually, Django is locating the file, and loading it automatically into the templates. There you go. Now you can use CSS in all your templates.


## An HTML Skeleton: How to set up a base structure to every Django template
As we've seen, it's pretty easy to add CSS files into Django template, but it would be quite exhaustive to need to always remember to add the CSS link to all templates we have in all our apps. If you're thinking that there must be a better way of doing this, you're absolutely right. What we need now is a base template. Let's create a templates folder in the static folder and a base.html template in it. Okay, so in here, we can create a normal HTML file, so html, then head, then in here, we can have link (keyboard clacks) type's going to be text/css, then href, it's going to be the same loading of a static file that we had, css/style.css, okay? Now, we have to remember to load static on the top of the file, load static, and, now, we can create a body, perfect. Now, what we need to do here is add the following command, so curly brackets and percentage block content, and then, similarly, we're going to do another one, but, now, it's endblock. Okay, so I call this content, but you can call it whatever you like. The important thing here is to know that this is a block area where we can inject things. Let's try it out. Let's go back to the notes and open the notes list template. So in here, what we can do is extends "base.html". Now, what we can do is get rid of all this basic HTML stuff here and use this block content here. So block content, and in here, we can endblock. Okay, so what we're doing here, we're taking only the important part of our template and wrapping it on the block content command so this can be injected on the base template. Let's try it out. Okay, so we have a problem here. The template is showing as non-existent. What happens here? So you can see here where Django was trying to search for a base HTML template. So you can see that it tried in multiple places, including the two templates folder in home and notes app, but as you can see, the static folder templates is not being looked for. So what we need to do is tell Django where to look for. So let's go back. Then in here, let's go to settings file, and down below, we're going to find out that there is a templates, and there is a list of directories that we can add here. So similar to what we did on the static files, we're going to add that particular folder in here. So let's do BASE_DIR, and then slash, and then static/templates, okay? So it reloaded. Let's try it again, and there you go. So let's take a minute to understand what's going on here. What's happening here is that with this syntax, we can define the basics of our HTML in our base.html template, and then we create each webpage as a separate template that extends the base. So we will build each template separately and just the small parts, but we'll then inject it to the base template where we can have all our default configurations, such as the CSS files and the JavaScripts. This will allow us to keep each webpage template as simple as we can while keeping all the configuration in a single place. That's another power of the Django template language. Now that you know exactly how to use a base template, I encourage you to go back and try it out in all the templates we have so far.

* If yo Need a Template please review Bulma [Framework](https://bulmatemplates.github.io/bulma-templates/templates/kanban.html)
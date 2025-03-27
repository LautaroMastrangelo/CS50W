#python web framework
django-admin startproject Project_Name #creates a Django "main" project
python manage.py runserver #creates the sv (needs to be in the created folder)
python manage.py startapp appName #creastes an app inside the project

from django.urls import path, include
path('appName/', include("app.urls")) #in main.urls.py
path("", views.function, name="chooseUrlName") #in app.urls.py
    #remember to create a function in views and import it to use views.

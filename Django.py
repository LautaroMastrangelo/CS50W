#python web framework
django-admin startproject Project_Name #creates a Django "main" project
python manage.py runserver #creates the sv (needs to be in the created folder)
python manage.py startapp appName #creastes an app inside the project

from django.urls import path, include

app_name = "appName"
urlpattenrs = [
path('appName/', include("app.urls")) #in main.urls.py
path("pageName {x}", views.function, name="chooseUrlName") #in app.urls.py
    #this are in different folders but follow the same logic
]
    #remember to create a function (like below) in views and import it to use views.
def functionName(request, parameter):
    return render(request, "appName/htmlFile.html", {"variableName":parameter}) #create a appName dir inside a templates one
    #path("<parameterType:parameterName>") allows ANY string in the **URL** to be used in the function

#Django html
{{ variableName }} #use a sent variable in html with django
{% if/for x %} #use logic inside this {% logic %}
    #html code EG: <li> {{x}} </li> display all elements in a python list
{% endif %}

<a href="{% url appName:pageName {x} %}"></a> #relative urls (adding appName to avoid mistakes)

{% load static %} #on top of the page to use relative rutes to a static (usually css) file
<link href="{% static 'dir/file.css' %}" rel="exampleRelation">

>create a html file that will be use as a layout
{% block blockname %} {% endblock %} #this will be edited on different html files using this layout
    #the rest of the html will be the same for all files that inherit this one
{% extends "layout.html" %} #at the top of the file
{% block blokcname %} code {% endblock %} #for every body that will be changed

class NewTaskForm(forms.Form) #on views.py, remember to import forms from Django
    field = forms.CharField(label="example")
#this class will be sent as an argument when loading the function inside the dic as: "form":NewTaskForm()

<form action="{link}" method="post">
{{ form }} #"import" a form from the view (explained above)
{% csrf_token %} #cybersecury mesure needed on Django
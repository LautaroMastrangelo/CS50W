#python web framework
django-admin startproject Project_Name #creates a Django "main" project
python manage.py runserver #creates the sv (needs to be in the created folder)
python manage.py startapp appName #creastes an app inside the project

from django.urls import path, include

app_name = "appName {x}" #this will be used to create a relative url (see below) 
urlpattenrs = [
path('', include("app.urls")) #in main.urls.py
path("<parameters>", views.function, name="pageName {x}") #in app.urls.py
    #this are in different folders but follow the same logic
]
    #remember to create a function (like below) in views and import it to use views.
def functionName(request, parameter):
    return render(request, "appName/htmlFile.html", {"variableName":parameter}) #need to create a appName dir inside a templates one
    # path("<parameterType:parameterName>", views, name) in the urls.py file 
        # allows ANY string in the **URL** to be used in the function

#Django html
{{ variableName }} #use a sent variable in html with django
{% if/for x %} #use logic inside this {% logic %}
{% empty %} #in case a for loop is empty
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

def viewsFunction(request): #client side validation
    if request.method == "POST" #access this post with request.POST, example below
    form = newTaskForm(request.POST) #form.is_valid() will check if the the form follows this class specifications 
    return render (request,samePage, {"form": form}) #will auto tell the error to the user
    #return HttpResponseRedirect(reverse(appName:pageName)) #a comfy way to redirect to other/same page
request.session #creates a session (which is a dictionary) for the current user
request.session["key"] = value #add a key to the session dict, for example a list 
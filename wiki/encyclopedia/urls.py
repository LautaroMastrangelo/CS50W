from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/random", views.randomPage, name="random"),
    
    path("wiki/<str:title>", views.entry, name="entry"),
]
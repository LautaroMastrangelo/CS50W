from django.shortcuts import render, redirect
import markdown2
from . import util
from django.http import HttpResponse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entry.html", 
        {"title":title, "content":markdown2.markdown(entry)})

def search(request):
    searchingFor = request.GET.get("q").lower()
    entry = util.get_entry(searchingFor)
    if entry is not None:
        return redirect("entry", title=searchingFor)
    else:
        return render(request, "encyclopedia/search.html", {
            "coincidences": list(filter(lambda c : searchingFor in c.lower(), util.list_entries()))
        })
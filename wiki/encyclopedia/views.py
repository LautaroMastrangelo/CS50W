from django.shortcuts import render
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

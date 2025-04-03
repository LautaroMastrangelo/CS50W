from django.shortcuts import render, redirect
import markdown2
from . import util
import random
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class newPageForm(forms.Form):
    title = forms.CharField(label="Page Title")
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        "placeholder": "Write here the page content and submit it!",
    }))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error404.html")
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

def randomPage(request):
    number = random.randint(0, len(util.list_entries()) -1)
    entries = util.list_entries()
    entry = entries[number]
    return redirect("entry", title=entry)

def createPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "form": newPageForm()
        })
    elif request.method == "POST":
        form = newPageForm(request.POST)
        if not form.is_valid():
            return render(request, "encyclopedia/create.html", {"form": form})
        else:
            title = form.cleaned_data["title"]
            entry = util.get_entry(title)
            if entry is not None:
                return render(request, "encyclopedia/error1.html", {"title": title})
            else:
                content = form.cleaned_data["content"]
                util.save_entry(title, content)
                return redirect("entry", title=title)
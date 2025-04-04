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

class editPageForm(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea())
                              
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
    def randomEntry():
        number = random.randint(0, len(util.list_entries()) -1)
        entries = util.list_entries()
        return entries[number]
    entry = randomEntry()
    try: #not really sure but this META function may not work on every browser so i added a try/except
        while entry in request.META.get("HTTP_REFERER", ""):
            entry = randomEntry()
    except:
        return redirect('index')    
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
                print(content)
                util.save_entry(title.title(), bytes(content, 'utf8'))
                return redirect("entry", title=title)

def editPage(request, title):
    if request.method == "GET":
        entry = util.get_entry(title)
        form = editPageForm(initial={"content": entry})
        return render(request, "encyclopedia/edit.html", {"title":title, "form": form,})
    else:
        form = editPageForm(request.POST)
        if not form.is_valid():
            return render(request, "encyclopedia/edit.html", {"title":title, "form": form})
        else:
            content = form.cleaned_data["content"]
            util.save_entry(title.title(), bytes(content, 'utf8'))
            return redirect("entry", title=title)
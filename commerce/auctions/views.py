from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listings, Bids, Comments, CATEGORIES

class ListingForm(forms.Form): 
    name = forms.CharField(label="Name", max_length=64)
    description = forms.CharField(label="Description", max_length=64)
    image = forms.ImageField(label="Image")
    startingBid = forms.DecimalField(label="Starting Bid", max_digits=10, decimal_places=2)
    category = forms.ChoiceField(label="Category", choices=[(category, category) for category in CATEGORIES])
    

def index(request):
    listings = Listings.objects.all()
    return render(request, "auctions/index.html",{
        "listings": listings
    })

def listing_item (request, listing_name, listing_id):
    return render(request, "auctions/listingItem.html", {
        "listing_name" : listing_name,
        "listing_id" : listing_id,
        "listing" : Listings.objects.get(id=listing_id),
    })

def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/createListing.html", {
            "form": ListingForm()
        })
    else:
        form = ListingForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "auctions/createListing.html", {
                "form": form
            })
        else:
            Listings.objects.create(
                lister=request.user,
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                image=form.cleaned_data["image"],
                startingBid=form.cleaned_data["startingBid"],
                category=form.cleaned_data["category"]
            )
            return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

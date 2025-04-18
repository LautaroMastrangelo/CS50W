from django.contrib.auth.models import AbstractUser
from django.db import models
import textwrap

CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home",
    "Books",
    "Sports",
    "Automotive",
    "Toys",
    "Health",
    "Collectibles",
    "Others"
]
class User(AbstractUser):
    watchlist = models.ManyToManyField('Listings', blank=True, related_name="watchers")

class Bids(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey('Listings', on_delete=models.CASCADE, related_name="bids")

class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=64)
    listing = models.ForeignKey('Listings', on_delete=models.CASCADE, related_name="comments")
    def __str__(self):
        return f"{self.commenter} - {self.comment} - {self.listing}"
    

class Listings(models.Model):
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    startingBid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=64, choices=[(category, category) for category in CATEGORIES])
    closed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} - {self.lister} - {self.startingBid} - {self.category} - {self.description} - {self.image}" 

    def price(self):
        return self.bids.filter().order_by("-amount").first().amount if self.bids.exists() else self.startingBid
    
    def currentBid(self):
        return self.bids.filter().order_by("-amount").first().amount if self.bids.exists() else 0
    
    def currentBider(self):
        return self.bids.filter().order_by("-amount").first().bidder if self.bids.exists() else None
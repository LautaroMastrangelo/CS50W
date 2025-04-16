from django.contrib.auth.models import AbstractUser
from django.db import models
import textwrap

CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home & Garden",
    "Books",
    "Sports & Outdoors",
    "Automotive",
    "Toys & Games",
    "Health & Beauty",
    "Collectibles",
    "Other"
]
class User(AbstractUser):
    pass

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
    image = models.ImageField(upload_to='images/')
    startingBid = models.IntegerField()
    category = models.CharField(max_length=64, choices=[(category, category) for category in CATEGORIES])
    def __str__(self):
        return f"{self.name} - {self.lister} - {self.startingBid} - {self.category} - {self.description} - {self.image}" 
    def __iter__(self):
        return iter([
        ("name", self.name),
        ("price", self.bids.filter().order_by("-amount").first() if self.bids.exists() else self.startingBid),
        ("description", self.description),
        ("category", self.category),
        ("lister", self.lister.username),
    ])

    def price(self):
        return self.bids.filter().order_by("-amount").first() if self.bids.exists() else self.startingBid
from django.contrib.auth.models import AbstractUser
from django.db import models
import textwrap
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.dispatch import receiver

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

    def __str__(self):
        return f"{self.username}"

class Bids(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey('Listings', on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.bidder} - {self.amount} - {self.listing.name}"

class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=64)
    listing = models.ForeignKey('Listings', on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.commenter} - {self.comment} - {self.listing.name}"
    
#I choose to use file images instead of URL because i wanted to practic it since i may need it for a future project of mine
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

#needed to delete images when deleting from admin/
@receiver(post_delete, sender=Listings)
def delete_listing_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
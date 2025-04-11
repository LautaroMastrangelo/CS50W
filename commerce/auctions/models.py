from django.contrib.auth.models import AbstractUser
from django.db import models
import textwrap
class User(AbstractUser):
    pass

class Bids(models.Model):
    pass

class Listings(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return (f"""- Name: {self.name}
                - Description: {self.description}
                - Price: ${self.price}""")
    
    def __iter__(self):
        return iter([
        ("name", self.name),
        ("description", self.description),
        ("price", self.price)
    ])
class comments(models.Model):
    pass

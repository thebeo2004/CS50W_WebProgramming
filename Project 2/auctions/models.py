from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model. This model is inherited from AbstractUser model. So in a default Django project, this model already has
    username, email, first_name, last_name, password, etc. fields. We can add more fields to this model if we want.
    """
    pass

class AuctionListing(models.Model):
    """
    A model for auction listing, stores information about auction items. This model has the following fields, corresponding to the properties displayed in the auction lists:
    title: title of the listing
    description: description of the listing
    starting_bid: starting bid of the listing
    image_url: image url of the listing
    category: category of the listing
    created_at: created time of the listing
    is_active: status of the listing
    owner: owner of the listing
    """
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(decimal_places=2, max_digits=10)
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=64, blank=True)
    created_at = models.TimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    
    def __str__(self):
        return f"{self.title} - {self.starting_bid}"
    
    
class Bid(models.Model):
    """
    A model for bid placed on listings. This model has the following fields, corresponding to the properties displayed in the bid lists:
    amount: amount of the bid
    listing: the listing of the bid
    bidder: the bidder of the bid
    created_at: created time of the bid
    """
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    created_at = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.amount} bid on {self.listing.title} by {self.bidder.username} at {self.created_at}"
    
class Comment(models.Model):
    """
    A model for storing comments on auction listings. This model has the following fields, corresponding to the properties displayed in the comment lists:
    content: content of the comment
    listing: the listing of the comment
    commenter: the commenter of the comment
    created_at: created time of the comment
    """
    content = models.TextField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.listing.title} at {self.created_at}"
    
    
    
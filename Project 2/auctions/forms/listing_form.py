from django import forms
from .models import AuctionListing

class ListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=[
                #First value: Actua value stored in the database
                #Second value: Human-readable label displayed in the dropdown
                ('', 'Select a category'),	
                ('Fashion', 'Fashion'),
                ('Toys', 'Toys'),
                ('Electronics', 'Electronics'),
                ('Home', 'Home'),
                ('Books', 'Books'),
                ('Sports', 'Sports'),
                ('Others', 'Others'),
                ]),
        }
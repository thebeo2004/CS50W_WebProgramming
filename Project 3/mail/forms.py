from django import forms
from .models import Email

class EmailComposeForm(forms.ModelForm):
    
    sender_email = forms.CharField(max_length=255,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'compose-sender'}),
                             label='From')
    
    recipient_emails = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'compose-recipients'}),
        label='To',)
    
    class Meta:
        model = Email
        fields = ['subject', 'body',]
        # exclude = ['user', 'sender', 'timestamp', 'read', 'archived']
        
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'compose-subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'id': 'compose-body'}),
        }
        
        labels = {
            'subject': '',
            'body': '',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sắp xếp lại thứ tự các trường
        self.order_fields(['sender_email', 'recipient_emails', 'subject', 'body'])
    
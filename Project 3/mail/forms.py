from django import forms
from .models import Email

class EmailComposeForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['sender', 'recipients', 'subject', 'body']
        # exclude = ['user', 'sender', 'timestamp', 'read', 'archived']
        
        widgets = {
            'sender': forms.TextInput(attrs={'class': 'form-control', 
                                            #  'readonly': 'readonly', 
                                             'disabled': 'disabled',
                                             'id': 'compose-sender'}),
            'recipients': forms.TextInput(attrs={'class': 'form-control',
                                                 'id': 'compose-recipients'}),
            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'compose-subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'id': 'compose-body'}),
        }
        
        labels = {
            'sender': 'From',
            'recipients': 'To',
            'subject': '',
            'body': '',
        }
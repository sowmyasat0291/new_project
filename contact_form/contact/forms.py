# contact/forms.py
from django import forms
from .models import Contact  # Import the renamed model

class ContactForm(forms.ModelForm):  # Now, no name conflict
    class Meta:
        model = Contact  # Use the correct model name
        fields = ('name', 'email', 'subject', 'message')
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'subject': 'Subject',
            'message': 'Message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        error_messages = {
            'name': {'required': 'Please enter your name.'},
            'email': {'required': 'Please enter your email.', 'invalid': 'Please enter a valid email address.'},
            'subject': {'required': 'Please enter a subject.'},
            'message': {'required': 'Please enter a message.'},
        }

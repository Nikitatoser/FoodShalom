from django import forms
from .models import Rates

class RatesForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['article', 'username', 'rating', 'comment']
        labels = {
            'article': 'Article',  # Translate field labels
            'username': 'Username',  # Add label for the new field
            'rating': 'Rating',
            'comment': 'Comment',
        }
        widgets = {
            'article': forms.Select(attrs={
                'class': 'form-control custom-select',
                'style': 'border-radius: 10px; background-color: #f8f9fa; font-size: 1.1em;'
            }),
            'username': forms.TextInput(attrs={  # Add widget for the new field
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'style': 'border-radius: 8px; background-color: #f1f3f5; font-family: "Arial", sans-serif;'
            }),
            'rating': forms.NumberInput(attrs={
                'type': 'range',
                'class': 'form-range',
                'min': 1.0,
                'max': 5.0,
                'step': 0.5,
                'style': 'width: 100%; margin: 10px 0;',
                'id': 'rating-range'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review here...',
                'style': 'border-radius: 8px; background-color: #f1f3f5; font-family: "Arial", sans-serif;'
            }),
        }


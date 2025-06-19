from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Review

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'comment']


class ReviewCreateNoModelForm(forms.Form):
    reviewer_name = forms.CharField(max_length=100)
    rating = forms.IntegerField(help_text="Enter a rating between 1 and 5", validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = forms.CharField(widget=forms.Textarea)
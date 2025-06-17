from django import forms

from .models import Book

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["author", "title", "number_of_pages", "published_on", "cover_image"]

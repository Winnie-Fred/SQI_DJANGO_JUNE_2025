from django import forms

from .models import Book
from authors.models import Author

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["author", "title", "number_of_pages", "published_on", "cover_image"]


class BookCreateNotModelForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    number_of_pages = forms.IntegerField()
    published_on = forms.DateField()
    cover_image = forms.ImageField(required=False)

from django import forms

from .models import Note, Category

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ["added_by"]

class FilterForm(forms.Form):
    category = forms.ChoiceField(choices=Category.choices, required=False)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
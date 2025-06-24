from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Note
from .forms import NoteForm, FilterForm, SearchForm, Category

# Create your views here.
def note_list(request):
    category_choices = Category.choices
    notes = Note.objects.all()
    filter_form = FilterForm()
    search_form = SearchForm()
    if request.method == "GET":
        filter_form = FilterForm(request.GET)
        if filter_form.is_valid():
            cleaned_data = filter_form.cleaned_data
            category = cleaned_data.get('category')
            if category:
                notes = notes.filter(category=category)
            
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            cleaned_data = search_form.cleaned_data
            query = cleaned_data.get('query')
            if query:
                notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))


    context = {
        "notes": notes,
        "filter_form": filter_form,
        "search_form": search_form,
        "category_choices": category_choices,
    }
    return render(request, "core/notes.html", context)

@login_required
def create_note(request):
    form = NoteForm()
    if request.method == "POST":
        user = request.user
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.added_by = user
            new_note.save()
            return redirect("core:notes")

        
    context = {
        'form': form
    }
    return render(request, "core/create-note.html", context) 

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "core/note-detail.html", {"note": note})



@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if note.added_by != request.user:
        messages.error(request, "You do not have permission to edit this note")
        return redirect("core:note_detail", note_id=note_id)
    
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("core:note_detail", note_id=note_id)
    context = {
        "note": note,
        "form": form
    }
    return render(request, "core/edit-note.html", context)

@login_required
def confirm_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if note.added_by != request.user:
        messages.error(request, "You do not have permission to delete this note")
    return render(request, "core/confirm-delete.html", {"note": note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if note.added_by != request.user:
        messages.error(request, "You do not have permission to delete this note")
    if request.method == "POST":
        note.delete()
        return redirect("core:notes")
    return redirect("core:note_detail", note_id=note_id)
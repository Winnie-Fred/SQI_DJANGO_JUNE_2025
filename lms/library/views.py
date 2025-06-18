from django.shortcuts import render, HttpResponse, redirect
from authors.models import Author
from .models import Book
from .forms import BookCreateForm, BookCreateNotModelForm

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "library/list-of-books.html", context)

def mvt(request):
    authors_ordered_by_birth_date = Author.objects.order_by("birth_date")
    all_authors = Author.objects.all()
    all_books = Book.objects.order_by("-title")

    context = {
        "authors": authors_ordered_by_birth_date,
        "books": all_books,
        "default_order": all_authors,
    }
    return render(request, "library/mvt.html", context)


def create_book(request):
    form = BookCreateForm()
    if request.method == "POST":
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:book_list')
    context = {
        'form': form
    }
    return render(request, "library/create-book.html", context)


def create_book_no_model_form(request):
    no_model_book_form = BookCreateNotModelForm()
    if request.method == "POST":
        no_model_book_form = BookCreateNotModelForm(request.POST, request.FILES)
        if no_model_book_form.is_valid():
            cleaned_data = no_model_book_form.cleaned_data
            # Book.objects.create(
            #     title=cleaned_data.get('title'),
            #     author=cleaned_data.get('author'),
            #     number_of_pages=cleaned_data.get('number_of_pages'),
            #     published_on=cleaned_data.get('published_on'),
            #     cover_image=cleaned_data.get('cover_image')
            # )
            Book.objects.create(**cleaned_data)
            return redirect('library:book_list')
    context = {
        'form': no_model_book_form
    }
    return render(request, "library/create-book-no-model-form.html", context)


def create_book_manually_rendered_form(request):
    form = BookCreateForm()
    if request.method == "POST":
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:book_list')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "library/create-book-manual-render.html", context)


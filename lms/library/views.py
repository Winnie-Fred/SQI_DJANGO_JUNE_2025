from django.shortcuts import render, HttpResponse
from authors.models import Author
from .models import Book
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
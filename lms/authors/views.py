from django.shortcuts import render

from .models import Author
from library.models import Book
from datetime import datetime

# Create your views here.

def all_authors(request):
    return render(request, "authors/authors.html")

def book_signings(request):
    return render(request, "authors/book-signings.html")

def mvt(request):
    # authors = Author.objects.all()
    authors = Author.objects.order_by('-last_name')
    all_books = Book.objects.all()

    # authors born before 2004
    year_2004 = datetime(2004, 1, 1)
    authors_born_before_2004 = Author.objects.filter(birth_date__lt=year_2004)
    try:
        special_author = Author.objects.get(pk=100)
    except Author.DoesNotExist:
        special_author = None
    
    context = {
        "all_authors": authors,
        "all_books": all_books,
        "special_author": special_author,
        "authors_born_before_2004": authors_born_before_2004,
    }
    return render(request, "authors/mvt.html", context)
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import Http404

from .models import Author
from .forms import AuthorCreateForm
from library.models import Book
from datetime import datetime

# Create your views here.

def all_authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, "authors/authors.html", context)

def author_detail(request, author_pk):
    # try:
    #     author = Author.objects.get(pk=author_pk)
    # except Author.DoesNotExist:
    #     raise Http404("Author matching query does not exist")
    
    author = get_object_or_404(Author, pk=author_pk)

    context = {"author": author}
    return render(request, "authors/author-detail.html", context)

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


def greet_me(request):
    return HttpResponse("Hello 👋")


def greet_me_required(request, name):
    return HttpResponse(f"Hello {name}👋")

def greet_me_optional(request):
    # print(request.GET)
    name = request.GET.get("name", "Anonymous")
    return HttpResponse(f"Hello {name}👋")

def create_author(request):
    author_create_form = AuthorCreateForm()
    if request.method == "POST":
        author_create_form = AuthorCreateForm(request.POST, request.FILES)
        if author_create_form.is_valid():
            author_create_form.save()
            return redirect('authors:all_authors')
    context = {
        "create_author_form": author_create_form
    }
        
    return render(request, "authors/create-author.html", context)


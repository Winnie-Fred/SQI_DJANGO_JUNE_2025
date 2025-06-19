from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from authors.models import Author
from .models import Book
from .forms import BookForm, BookNotModelForm

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
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:book_list')
    context = {
        'form': form
    }
    return render(request, "library/create-book.html", context)


def create_book_no_model_form(request):
    no_model_book_form = BookNotModelForm()
    if request.method == "POST":
        no_model_book_form = BookNotModelForm(request.POST, request.FILES)
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
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:book_list')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "library/create-book-manual-render.html", context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "library/book-detail.html", {'book': book})

def update_book_model_form(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:book_list')
    context = {
        'form': form,
        'book': book
    }
    return render(request, "library/update-book-model-form.html", context=context)


def update_book_no_model_form(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookNotModelForm(initial={
        'title': book.title,
        'author': book.author,
        'number_of_pages': book.number_of_pages,
        'published_on': book.published_on,
        'cover_image': book.cover_image,
    })
    if request.method == "POST":
        form = BookNotModelForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            book.title = cleaned_data.get('title')
            book.author = cleaned_data.get('author')
            book.number_of_pages = cleaned_data.get('number_of_pages')
            book.published_on = cleaned_data.get('published_on')
            book.cover_image = cleaned_data.get('cover_image')
            book.save()
            return redirect('library:book_list')
    context = {
        'form': form,
        'book': book
    }
    return render(request, "library/update-book-no-model-form.html", context=context)



def confirm_delete(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, "library/confirm-delete.html", {"book": book})


def delete_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == "POST":
        book.delete()
        return redirect("library:book_list")
    return redirect("library:book_detail", book_id=book_pk)
from django.shortcuts import render, get_object_or_404

from .models import Book

# Create your views here.
def home(request):
    return render(request, "review/index.html")


def book_list(request):
    all_books = Book.objects.all()
    context = {"all_books": all_books}
    return render(request, "review/all-books.html", context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "review/book-detail.html", {"book": book})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Book, Review
from .forms import ReviewForm
from .decorators import user_owns_review

# Create your views here.
def home(request):
    featured_books = Book.objects.filter(is_featured=True)
    return render(request, "review/index.html", {"featured": featured_books})


def book_list(request):
    all_books = Book.objects.all()
    context = {"all_books": all_books}
    return render(request, "review/all-books.html", context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if not request.user.is_authenticated:
            messages.error(request, f'You need to log in to leave a review on "{book.title}"')
            return redirect("users:login")
        
        if form.is_valid():
            review = form.save(commit=False)
            review.added_by = request.user
            review.book = book
            review.save()
            return redirect("review:book_detail", book_id=book_id)

    context = {"book": book, "form": form}
    return render(request, "review/book-detail.html", context)

@login_required
@user_owns_review("edit")
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    
    if not review.can_still_edit():
        messages.info(request, "You cannot edit a review 5 minutes after creating it. Maybe delete it instead?")
        return redirect("review:book_detail", book_id=review.book.pk)

    
    form = ReviewForm(instance=review)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("review:book_detail", book_id=review.book.pk)
        
    context = {
        "form": form,
        "review": review
    }
    return render(request, "review/edit-review.html", context)


@login_required
@user_owns_review("delete")
def confirm_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, "review/confirm-delete.html", {"review": review})


@login_required
@user_owns_review("delete")
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        review.delete()
    return redirect("review:book_detail", book_id=review.book.id)

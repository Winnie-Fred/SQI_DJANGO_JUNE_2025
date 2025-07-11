from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Book, Review
from .forms import ReviewForm, ReviewCreateNoModelForm, ReviewUpdateNoModelForm

# Create your views here.
def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "review/book-list.html", context)


def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    review_create_form = ReviewForm()
    if request.method == "POST":
        review_create_form = ReviewForm(request.POST)
        if review_create_form.is_valid():
            review = review_create_form.save(commit=False)
            review.book = book
            review.save()
            return redirect('review:book_detail', book_pk=book_pk)
    context = {
        'book': book,
        'review_create_form': review_create_form
    }
    return render(request, "review/book-detail.html", context)


def book_detail_no_model_form(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_create_form = ReviewCreateNoModelForm()
    if request.method == "POST":
        review_create_form = ReviewCreateNoModelForm(request.POST)
        if review_create_form.is_valid():
            cleaned_data = review_create_form.cleaned_data
            print(cleaned_data)
            # Review.objects.create(
            #     reviewer_name=cleaned_data.get('reviewer_name'),
            #     comment=cleaned_data.get('comment'),
            #     rating=cleaned_data.get('rating'),
            #     book=book
            # )
            Review.objects.create(**cleaned_data, book=book)
            return redirect('review:book_detail_no_model_form', book_id=book_id)
    context = {
        'book': book,
        'review_create_form': review_create_form
    }
    return render(request, "review/book-detail-no-model-form.html", context)


def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    book_id = review.book.pk
    review_form = ReviewUpdateNoModelForm(initial={
        'rating': review.rating,
        'comment': review.comment,
    })
    if request.method == "POST":
        review_form = ReviewUpdateNoModelForm(request.POST)
        if review_form.is_valid():
            cleaned_data = review_form.cleaned_data
            review.rating = cleaned_data.get("rating")
            review.comment = cleaned_data.get("comment")
            review.save()
            return redirect("review:book_detail_no_model_form", book_id=book_id)
    context = {
        "form": review_form,
        "review": review,
    }
    return render(request, "review/edit-review.html", context)
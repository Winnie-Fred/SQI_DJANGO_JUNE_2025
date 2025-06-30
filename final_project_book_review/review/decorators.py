from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from functools import wraps
from .models import Review

def user_owns_review(action="modify"):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            review_id = kwargs.get("review_id")
            if not review_id:
                messages.error(request, f"No review specified to {action}.")
                return redirect("review:book_list")

            review = get_object_or_404(Review, pk=review_id)

            if review.added_by != request.user:
                messages.error(request, f"You do not have permission to {action} this review.")
                return redirect("review:book_detail", book_id=review.book.id)

            request.review = review
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

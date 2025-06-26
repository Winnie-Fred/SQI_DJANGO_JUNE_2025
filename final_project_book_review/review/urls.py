from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("", views.home, name="home"),
    path('books/all/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('edit/review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('confirm-delete/review/<int:review_id>/', views.confirm_delete, name='confirm_delete'),
    path('delete/review/<int:review_id>/', views.delete_review, name='delete_review'),
]
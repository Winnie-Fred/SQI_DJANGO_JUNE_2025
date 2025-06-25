from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("", views.home, name="home"),
    path('books/all/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
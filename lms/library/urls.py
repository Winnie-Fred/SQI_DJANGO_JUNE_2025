from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('mvt/', views.mvt, name='library-mvt'),
    path('create/book/', views.create_book, name='create_book'),
]
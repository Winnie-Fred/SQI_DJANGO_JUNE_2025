from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [
    path('', views.all_authors, name='all_authors'),
    path('book-signings/', views.book_signings, name='book_signings'),
    path('mvt/', views.mvt, name='mvt'),
    path('author/<int:author_pk>/', views.author_detail, name="author_detail"),
    # path('greet/me/<str:name>/', views.greet_me_required, name='greet_me_required'),
    # path('greet/me/', views.greet_me, name='greet_me'),
    path('greet/me/', views.greet_me_optional, name='greet_me_optional'),
    path('create/author/', views.create_author, name='create_author'),
]
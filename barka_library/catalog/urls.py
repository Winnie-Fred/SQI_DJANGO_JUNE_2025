from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('special/', views.featured_books, name='featured_books'),
]
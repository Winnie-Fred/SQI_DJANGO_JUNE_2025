from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('mvt/', views.mvt, name='library-mvt'),
    path('create/book/', views.create_book, name='create_book'),
    path('create/book/no-model-form/', views.create_book_no_model_form, name='create_book_no_model_form'),
    path('create/book/manual-render/', views.create_book_manually_rendered_form, name='create_book_manually_rendered_form'),
    path('update/book/<int:book_id>/', views.update_book_model_form, name='update_book_model_form'),
    path('update/book/no-model-form/<int:book_id>/', views.update_book_no_model_form, name='update_book_no_model_form'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('confirm-delete/book/<int:book_pk>/', views.confirm_delete, name='confirm_delete'),
    path('delete/book/<int:book_pk>/', views.delete_book, name='delete_book'),
]
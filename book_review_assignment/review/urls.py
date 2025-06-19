from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_pk>', views.book_detail, name='book_detail'),
    path('book/no-model-form/<int:book_id>', views.book_detail_no_model_form, name='book_detail_no_model_form'),
]
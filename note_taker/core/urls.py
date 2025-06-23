from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.note_list, name='notes'),
    path('notes/new/', views.create_note, name='create_note'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('edit/note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('confirm-delete/note/<int:note_id>/', views.confirm_delete, name='confirm_delete'),
    path('delete/note/<int:note_id>/', views.delete_note, name='delete_note'),
]
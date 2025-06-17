from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artists, name='artists'),
    path('albums/', views.albums, name='albums'),
    path('artist_detail/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
]
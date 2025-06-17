from django.shortcuts import render , get_object_or_404

from .models import Artist, Album

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def artists(request):
    context = {
        'artists': Artist.objects.order_by('debut_year'),
    }
    return render(request, "core/artists.html", context)


def albums(request):
    context = {
        'albums': Album.objects.order_by('release_date'),
    }
    return render(request, "core/albums.html", context)

def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    context = {"artist": artist}
    return render(request, "core/artist_detail.html", context)

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "core/album_detail.html", {"album": album})
from django.shortcuts import render

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
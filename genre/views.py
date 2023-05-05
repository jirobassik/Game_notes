from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GameGenreForm
from genre.models import GameGenreModel

from utils.request_server import Request
from utils.json_serializer import JsonSerializer
from .serializers import GenreSerializer

genre_json_serializer = JsonSerializer(GameGenreModel, GenreSerializer)
genre_request = Request.genre_model()


def add_genre(request):
    if request.method == 'POST':
        form = GameGenreForm(request.POST)
        if form.is_valid():
            serializer_data = genre_json_serializer.encode(name=form.cleaned_data['name'],
                                                           description=form.cleaned_data['description'], )

            genre_request.post_request(serializer_data)
        return HttpResponseRedirect(reverse('genre'))

    else:
        form = GameGenreForm()
    return render(request, 'genre/create_genre.html', {'form': form})


def edit_genre(request, pk=None):
    raw_data_platform = genre_request.detail_get_request(pk)
    queryset_platform = genre_json_serializer.detail_decode(raw_data_platform)
    if request.method == 'POST':
        form = GameGenreForm(request.POST)
        if form.is_valid():
            serializer_data = genre_json_serializer.encode(name=form.cleaned_data['name'],
                                                           description=form.cleaned_data['description'], )

            genre_request.put_request(serializer_data, pk)
        return HttpResponseRedirect(reverse('genre'))
    else:
        form = GameGenreForm(initial=queryset_platform)
    return render(request, 'genre/update_genre.html', {'form': form})


def view_genres(request):
    raw_data_genre = genre_request.get_request()
    queryset_genre = genre_json_serializer.decode(raw_data_genre)
    return render(request, 'genre/genre.html', {'genres': queryset_genre})


def detail_view_genres(request, pk=None):
    raw_data = genre_request.detail_get_request(pk)
    queryset = genre_json_serializer.detail_decode(raw_data)
    return render(request, 'genre/view_genre.html', {'platform': queryset})


def delete_genre(request, pk=None):
    genre_request.delete_request(pk)
    return HttpResponseRedirect(reverse('genre'))

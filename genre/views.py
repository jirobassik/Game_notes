from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import GameGenreForm
from utils.init_json_ser_req import genre_json_serializer, genre_request


def serialize_genre_form(form):
    return genre_json_serializer.encode(name=form.cleaned_data['name'],
                                        description=form.cleaned_data['description'], )


def add_genre(request):
    if request.method == 'POST':
        form = GameGenreForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_genre_form(form)
            genre_request.post_request(serializer_data)
        return HttpResponseRedirect(reverse('genre'))
    else:
        form = GameGenreForm()
    return render(request, 'genre/create_genre.html', {'form': form})


def edit_genre(request, pk=None):
    raw_data_platform = genre_request.detail_get_request(pk)
    queryset_platform = genre_json_serializer.decode(raw_data_platform, many=False)
    if request.method == 'POST':
        form = GameGenreForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_genre_form(form)
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
    queryset = genre_json_serializer.decode(raw_data, many=False)
    return render(request, 'genre/view_genre.html', {'genre': queryset})


def delete_genre(request, pk=None):
    genre_request.delete_request(pk)
    return HttpResponseRedirect(reverse('genre'))

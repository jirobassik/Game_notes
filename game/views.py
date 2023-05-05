from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import GameModel
from .forms import GameForm
from genre.models import GameGenreModel
from genre.serializers import GenreSerializer
from utils.request_server import Request
from utils.json_serializer import JsonSerializer
from .serializers import GameSerializer

game_json_serializer = JsonSerializer(GameModel, GameSerializer)
genre_json_serializer = JsonSerializer(GameGenreModel, GenreSerializer)
game_request = Request.game_model()
genre_request = Request.genre_model()


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            serializer_data = game_json_serializer.encode(name=form.cleaned_data['name'],
                                                          description=form.cleaned_data['description'],
                                                          publisher=form.cleaned_data['publisher'],
                                                          developer=form.cleaned_data['developer'],
                                                          genres=form.cleaned_data['genres'],
                                                          game_platform=form.cleaned_data['game_platform'],
                                                          buy=form.cleaned_data['buy'],
                                                          beta=form.cleaned_data['beta'],
                                                          passed=form.cleaned_data['passed'])
            game_request.post_request(serializer_data)
            return HttpResponseRedirect(reverse('game'))
    else:
        form = GameForm()
    return render(request, 'game/create_game.html', {'form': form})


def view_game(request):
    raw_data = game_request.get_request()
    queryset = game_json_serializer.decode(raw_data)
    return render(request, 'game/game.html', {'games': queryset})


def detail_view_game(request, pk=None):
    raw_data = game_request.detail_get_request(pk)
    queryset = game_json_serializer.detail_decode(raw_data)
    return render(request, 'game/view_game.html', {'game': queryset})


def edit_game(request, pk=None):
    raw_data = game_request.detail_get_request(pk)
    queryset = game_json_serializer.detail_decode(raw_data)
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            serializer_data = game_json_serializer.encode(name=form.cleaned_data['name'],
                                                          description=form.cleaned_data['description'],
                                                          publisher=form.cleaned_data['publisher'],
                                                          developer=form.cleaned_data['developer'],
                                                          genres=form.cleaned_data['genres'],
                                                          game_platform=form.cleaned_data['game_platform'],
                                                          buy=form.cleaned_data['buy'],
                                                          beta=form.cleaned_data['beta'],
                                                          passed=form.cleaned_data['passed'])
            game_request.put_request(serializer_data, pk)
            return HttpResponseRedirect(reverse('game'))
    else:
        form = GameForm(initial=queryset)
    return render(request, 'game/edit_game.html', {'form': form})


def delete_game(request, pk=None):
    game_request.delete_request(pk)
    return HttpResponseRedirect(reverse('game'))

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import GameForm
from utils.init_json_ser_req import game_json_serializer, game_request


def serialize_game_form(form):
    return game_json_serializer.encode(name=form.cleaned_data['name'],
                                       description=form.cleaned_data['description'],
                                       publisher=form.cleaned_data['publisher'],
                                       developer=form.cleaned_data['developer'],
                                       genres=form.cleaned_data['genres'],
                                       game_platform=form.cleaned_data['game_platform'],
                                       buy=form.cleaned_data['buy'],
                                       beta=form.cleaned_data['beta'],
                                       passed=form.cleaned_data['passed'])


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_game_form(form)
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
    queryset = game_json_serializer.decode(raw_data, many=False)
    return render(request, 'game/view_game.html', {'game': queryset})


def edit_game(request, pk=None):
    raw_data = game_request.detail_get_request(pk)
    queryset = game_json_serializer.decode(raw_data, many=False)
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_game_form(form)
            game_request.put_request(serializer_data, pk)
            return HttpResponseRedirect(reverse('game'))
    else:
        form = GameForm(initial=queryset)
    return render(request, 'game/edit_game.html', {'form': form})


def delete_game(request, pk=None):
    game_request.delete_request(pk)
    return HttpResponseRedirect(reverse('game'))

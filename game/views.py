from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from .models import GameModel
from .forms import GameForm


class Game(ListView):
    model = GameModel
    template_name = 'game/game.html'
    context_object_name = 'games'


class GameCreate(CreateView):
    model = GameModel
    form_class = GameForm
    template_name = 'game/create_game.html'
    success_url = reverse_lazy("game")


class GameUpdate(UpdateView):
    model = GameModel
    form_class = GameForm
    template_name = 'game/edit_game.html'
    success_url = reverse_lazy("game")


class GameView(DetailView):
    model = GameModel
    template_name = 'game/view_game.html'
    context_object_name = 'game'


class GameDelete(DeleteView):
    model = GameModel
    context_object_name = 'game'
    success_url = reverse_lazy("game")

    def form_valid(self, form):
        messages.success(self.request, "Игра была успешна удалена.")
        return super(GameDelete, self).form_valid(form)

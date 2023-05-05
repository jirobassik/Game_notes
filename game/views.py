from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from .models import GameModel
# from .forms import GameForm


from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.request_server import decode, delete_request
from .serializers import GameSerializer

class GameList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'game/game.html'

    @staticmethod
    def get(request):
        print('request data', request.path)
        queryset = decode()
        return Response({'games': queryset})

def add(request):
    form = GameSerializer
    return render(request, 'game/create_game.html', {'form': form})

def view(request):
    queryset = decode()
    return render(request, 'game/game.html', {'games': queryset})

def delete(request, pk=None):
    delete_request(pk)
    return HttpResponseRedirect(reverse('game'))


class GameDelete(APIView):

    @staticmethod
    def delete(request, pk=None):
        delete_request(pk)
        return HttpResponseRedirect(reverse_lazy('game'))


# class Game(ListView):
#     model = GameModel
#     template_name = 'game/game.html'
#     context_object_name = 'games'


# class GameCreate(CreateView):
#     model = GameModel
#     form_class = GameForm
#     template_name = 'game/create_game.html'
#     success_url = reverse_lazy("game")
#
#
# class GameUpdate(UpdateView):
#     model = GameModel
#     form_class = GameForm
#     template_name = 'game/edit_game.html'
#     success_url = reverse_lazy("game")


# class GameView(DetailView):
#     model = GameModel
#     template_name = 'game/view_game.html'
#     context_object_name = 'game'


# class GameDelete(DeleteView):
#     model = GameModel
#     context_object_name = 'game'
#     success_url = reverse_lazy("game")
#
#     def form_valid(self, form):
#         messages.success(self.request, "Игра была успешна удалена.")
#         return super(GameDelete, self).form_valid(form)

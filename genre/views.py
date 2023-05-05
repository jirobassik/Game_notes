from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from .models import GameGenreModel
# from .forms import GenreForm


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import GameGenreModel
from .forms import GameGenreForm
from genre.models import GameGenreModel
from genre.serializers import GenreSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.request_server import Request
from utils.json_serializer import JsonSerializer
from .serializers import GenreSerializer

genre_json_serializer = JsonSerializer(GameGenreModel, GenreSerializer)
genre_request = Request.genre_model()

def add_genre(request):
    standart_form = GameGenreForm
    return render(request, 'genre/create_genre.html', {'form': standart_form})

def view_genres(request):
    raw_data_genre = genre_request.get_request()
    queryset_genre = genre_json_serializer.decode(raw_data_genre)
    return render(request, 'genre/genre.html', {'genres': queryset_genre})

def delete_genre(request, pk=None):
    genre_request.delete_request(pk)
    return HttpResponseRedirect(reverse('genre'))







#
# class Genre(ListView):
#     model = GameGenreModel
#     template_name = 'genre/genre.html'
#     context_object_name = 'genres'
#
# class GenreView(DetailView):
#     model = GameGenreModel
#     template_name = 'genre/view_genre.html'
#     context_object_name = 'genre'
#
# class GenreCreate(CreateView):
#     model = GameGenreModel
#     form_class = GenreForm
#     template_name = 'genre/create_genre.html'
#     success_url = reverse_lazy("genre")
#
#
# class GenreUpdate(UpdateView):
#     model = GameGenreModel
#     form_class = GenreForm
#     template_name = 'genre/update_genre.html'
#     success_url = reverse_lazy("genre")
#
#
# class GenreDelete(DeleteView):
#     model = GameGenreModel
#     context_object_name = 'genre'
#     success_url = reverse_lazy("genre")
#
#     def form_valid(self, form):
#         messages.success(self.request, "Жанр был успешно удален.")
#         return super(GenreDelete, self).form_valid(form)

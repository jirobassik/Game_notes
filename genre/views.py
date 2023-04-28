from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from .models import GameGenreModel
from .forms import GenreForm


class Genre(ListView):
    model = GameGenreModel
    template_name = 'genre/genre.html'
    context_object_name = 'genres'

class GenreView(DetailView):
    model = GameGenreModel
    template_name = 'genre/view_genre.html'
    context_object_name = 'genre'

class GenreCreate(CreateView):
    model = GameGenreModel
    form_class = GenreForm
    template_name = 'genre/create_genre.html'
    success_url = reverse_lazy("genre")


class GenreUpdate(UpdateView):
    model = GameGenreModel
    form_class = GenreForm
    template_name = 'genre/update_genre.html'
    success_url = reverse_lazy("genre")


class GenreDelete(DeleteView):
    model = GameGenreModel
    context_object_name = 'genre'
    success_url = reverse_lazy("genre")

    def form_valid(self, form):
        messages.success(self.request, "Жанр был успешно удален.")
        return super(GenreDelete, self).form_valid(form)

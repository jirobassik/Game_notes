from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from .models import GamePlatformModel
from .forms import GamePlatformForm


class GamePlatform(ListView):
    model = GamePlatformModel
    template_name = 'game_platform/game_platform.html'
    context_object_name = 'platforms'


class GamePlatformCreate(CreateView):
    model = GamePlatformModel
    form_class = GamePlatformForm
    template_name = 'game_platform/create_platform.html'
    success_url = reverse_lazy("platform")


class GamePlatformUpdate(UpdateView):
    model = GamePlatformModel
    form_class = GamePlatformForm
    template_name = 'game_platform/edit_platform.html'
    success_url = reverse_lazy("platform")


class GamePlatformView(DetailView):
    model = GamePlatformModel
    template_name = 'game_platform/view_platform.html'
    context_object_name = 'platform'


class GamePlatformDelete(DeleteView):
    model = GamePlatformModel
    context_object_name = 'platform'
    success_url = reverse_lazy("platform")

    def form_valid(self, form):
        messages.success(self.request, "Игра была успешна удалена.")
        return super(GamePlatformDelete, self).form_valid(form)

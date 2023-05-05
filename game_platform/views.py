from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import GamePlatformModel
# from .forms import GameGenreForm
from genre.models import GameGenreModel
from genre.serializers import GenreSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.request_server import Request
from utils.json_serializer import JsonSerializer
from .serializers import GamePlatformSerializer

platform_json_serializer = JsonSerializer(GamePlatformModel, GenreSerializer)
platform_request = Request.platform_model()


# def add_platform(request):
#     standart_form = GameGenreForm
#     return render(request, 'genre/create_genre.html', {'form': standart_form})


def view_platform(request):
    raw_data_platform = platform_request.get_request()
    queryset_platform = platform_json_serializer.decode(raw_data_platform)
    return render(request, 'game_platform/game_platform.html', {'platforms': queryset_platform})


def delete_platform(request, pk=None):
    platform_request.delete_request(pk)
    return HttpResponseRedirect(reverse('platform'))

#
# class GamePlatform(ListView):
#     model = GamePlatformModel
#     template_name = 'game_platform/game_platform.html'
#     context_object_name = 'platforms'
#
#
# class GamePlatformCreate(CreateView):
#     model = GamePlatformModel
#     form_class = GamePlatformForm
#     template_name = 'game_platform/create_platform.html'
#     success_url = reverse_lazy("platform")
#
#
# class GamePlatformUpdate(UpdateView):
#     model = GamePlatformModel
#     form_class = GamePlatformForm
#     template_name = 'game_platform/edit_platform.html'
#     success_url = reverse_lazy("platform")
#
#
# class GamePlatformView(DetailView):
#     model = GamePlatformModel
#     template_name = 'game_platform/view_platform.html'
#     context_object_name = 'platform'
#
#
# class GamePlatformDelete(DeleteView):
#     model = GamePlatformModel
#     context_object_name = 'platform'
#     success_url = reverse_lazy("platform")
#
#     def form_valid(self, form):
#         messages.success(self.request, "Игра была успешна удалена.")
#         return super(GamePlatformDelete, self).form_valid(form)

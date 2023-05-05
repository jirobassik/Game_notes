from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import GamePlatformModel
from .forms import GamePlatformForm

from utils.request_server import Request
from utils.json_serializer import JsonSerializer
from .serializers import GamePlatformSerializer

platform_json_serializer = JsonSerializer(GamePlatformModel, GamePlatformSerializer)
platform_request = Request.platform_model()


def add_platform(request):
    if request.method == 'POST':
        form = GamePlatformForm(request.POST)
        if form.is_valid():
            serializer_data = platform_json_serializer.encode(name=form.cleaned_data['name'],
                                                              description=form.cleaned_data['description'], )

            platform_request.post_request(serializer_data)
        return HttpResponseRedirect(reverse('platform'))

    else:
        form = GamePlatformForm()
    return render(request, 'game_platform/create_platform.html', {'form': form})


def edit_platform(request, pk=None):
    raw_data_platform = platform_request.detail_get_request(pk)
    queryset_platform = platform_json_serializer.detail_decode(raw_data_platform)
    if request.method == 'POST':
        form = GamePlatformForm(request.POST)
        if form.is_valid():
            serializer_data = platform_json_serializer.encode(name=form.cleaned_data['name'],
                                                              description=form.cleaned_data['description'], )

            platform_request.put_request(serializer_data, pk)
        return HttpResponseRedirect(reverse('platform'))

    else:
        form = GamePlatformForm(initial=queryset_platform)
    return render(request, 'game_platform/edit_platform.html', {'form': form})


def detail_view_platform(request, pk=None):
    raw_data = platform_request.detail_get_request(pk)
    queryset = platform_json_serializer.detail_decode(raw_data)
    return render(request, 'game_platform/view_platform.html', {'platform': queryset})


def view_platform(request):
    raw_data_platform = platform_request.get_request()
    queryset_platform = platform_json_serializer.decode(raw_data_platform)
    return render(request, 'game_platform/game_platform.html', {'platforms': queryset_platform})


def delete_platform(request, pk=None):
    platform_request.delete_request(pk)
    return HttpResponseRedirect(reverse('platform'))

from django.shortcuts import render
from .forms import GamePlatformForm

from utils.init_json_ser_req import platform_json_serializer, platform_request


def serialize_platform_form(form):
    return platform_json_serializer.encode(name=form.cleaned_data['name'],
                                           description=form.cleaned_data['description'], )


def add_platform(request):
    if request.method == 'POST':
        form = GamePlatformForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_platform_form(form)
            platform_request.post_request(serializer_data)
            raw_data_platform = platform_request.get_request()
            queryset_platform = platform_json_serializer.decode(raw_data_platform)
            return render(request, 'game_platform/game_platform.html', {'platforms': queryset_platform})
    else:
        form = GamePlatformForm()
    return render(request, 'game_platform/create_platform.html', {'form': form})


def edit_platform(request, pk=None):
    raw_data_platform = platform_request.detail_get_request(pk)
    queryset_platform = platform_json_serializer.decode(raw_data_platform, many=False)
    if request.method == 'POST':
        form = GamePlatformForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_platform_form(form)
            platform_request.put_request(serializer_data, pk)
            raw_data_platform = platform_request.get_request()
            queryset_platform = platform_json_serializer.decode(raw_data_platform)
            return render(request, 'game_platform/game_platform.html', {'platforms': queryset_platform})
    else:
        form = GamePlatformForm(initial=queryset_platform)
    return render(request, 'game_platform/edit_platform.html', {'form': form, 'pk': pk})


def detail_view_platform(request, pk=None):
    raw_data = platform_request.detail_get_request(pk)
    queryset = platform_json_serializer.decode(raw_data, many=False)
    return render(request, 'game_platform/view_platform.html', {'platform': queryset})


def view_platform(request):
    raw_data_platform = platform_request.get_request()
    queryset_platform = platform_json_serializer.decode(raw_data_platform)
    return render(request, 'game_platform/game_platform.html', {'platforms': queryset_platform})


def delete_platform(request, pk=None):
    platform_request.delete_request(pk)
    raw_data_platform = platform_request.get_request()
    queryset_platform = platform_json_serializer.decode(raw_data_platform)
    return render(request, 'game_platform/game_platform.html', {'platforms': queryset_platform})

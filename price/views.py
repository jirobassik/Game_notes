from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import GamePriceModel
from .forms import PriceForm
from utils.request_server import Request
from utils.json_serializer import JsonSerializer
from utils.converter_remove import remove_dollar
from .serializers import GamePriceSerializer

price_json_serializer = JsonSerializer(GamePriceModel, GamePriceSerializer)
price_request = Request.price_model()


def add_price(request):
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            serializer_data = price_json_serializer.encode(name=form.cleaned_data['name'],
                                                           price=form.cleaned_data['price'],
                                                           game=form.cleaned_data['game'],
                                                           price_currency="USD")

            price_request.post_request(serializer_data)
        return HttpResponseRedirect(reverse('price'))

    else:
        form = PriceForm()
    return render(request, 'price/create_price.html', {'form': form})


def edit_price(request, pk=None):
    raw_data_platform = price_request.detail_get_request(pk)
    queryset_platform = price_json_serializer.detail_decode(raw_data_platform)
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            serializer_data = price_json_serializer.encode(name=form.cleaned_data['name'],
                                                           price=form.cleaned_data['price'],
                                                           game=form.cleaned_data['game'],
                                                           price_currency="USD")
            price_request.put_request(serializer_data, pk)
        return HttpResponseRedirect(reverse('price'))
    else:
        form = PriceForm(initial=remove_dollar(queryset_platform))
    return render(request, 'price/edit_price.html', {'form': form})

def detail_view_price(request, pk=None):
    raw_data = price_request.detail_get_request(pk)
    queryset = price_json_serializer.detail_decode(raw_data)
    return render(request, 'price/view_price.html', {'price': queryset})

def view_price(request):
    raw_data_genre = price_request.get_request()
    queryset_genre = price_json_serializer.decode(raw_data_genre)
    return render(request, 'price/price.html', {'prices': queryset_genre})


def delete_price(request, pk=None):
    price_request.delete_request(pk)
    return HttpResponseRedirect(reverse('price'))

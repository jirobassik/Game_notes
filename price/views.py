from django.shortcuts import render
from .forms import PriceForm
from utils.converter_remove import remove_dollar
from utils.init_json_ser_req import price_json_serializer, price_request


def serialize_price_form(form):
    return price_json_serializer.encode(name=form.cleaned_data['name'],
                                        price=form.cleaned_data['price'],
                                        game=form.cleaned_data['game'],
                                        price_currency="USD")


def add_price(request):
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_price_form(form)
            price_request.post_request(serializer_data)
        raw_data_genre = price_request.get_request()
        queryset_genre = price_json_serializer.decode(raw_data_genre)
        return render(request, 'price/price.html', {'prices': queryset_genre})
    else:
        form = PriceForm()
    return render(request, 'price/create_price.html', {'form': form})


def edit_price(request, pk=None):
    raw_data_price = price_request.detail_get_request(pk)
    queryset_price = price_json_serializer.decode(raw_data_price, many=False)
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            serializer_data = serialize_price_form(form)
            price_request.put_request(serializer_data, pk)
        raw_data_price = price_request.get_request()
        queryset_price = price_json_serializer.decode(raw_data_price)
        return render(request, 'price/price.html', {'prices': queryset_price})
    else:
        form = PriceForm(initial=remove_dollar(queryset_price))
    return render(request, 'price/edit_price.html', {'form': form, 'pk': pk})


def detail_view_price(request, pk=None):
    raw_data = price_request.detail_get_request(pk)
    queryset = price_json_serializer.decode(raw_data, many=False)
    return render(request, 'price/view_price.html', {'price': queryset})


def view_price(request):
    raw_data_price = price_request.get_request()
    queryset_price = price_json_serializer.decode(raw_data_price)
    return render(request, 'price/price.html', {'prices': queryset_price})


def delete_price(request, pk=None):
    price_request.delete_request(pk)
    raw_data_price = price_request.get_request()
    queryset_price = price_json_serializer.decode(raw_data_price)
    return render(request, 'price/price.html', {'prices': queryset_price})

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from .models import GamePriceModel
from .forms import PriceForm

class Price(ListView):
    model = GamePriceModel
    template_name = 'price/price.html'
    context_object_name = 'prices'


class PriceCreate(CreateView):
    model = GamePriceModel
    form_class = PriceForm
    template_name = 'price/create_price.html'
    success_url = reverse_lazy("price")

class PriceUpdate(UpdateView):
    model = GamePriceModel
    form_class = PriceForm
    template_name = 'price/edit_price.html'
    success_url = reverse_lazy("price")

class PriceView(DetailView):
    model = GamePriceModel
    template_name = 'price/view_price.html'
    context_object_name = 'price'

class PriceDelete(DeleteView):
    model = GamePriceModel
    context_object_name = 'price'
    success_url = reverse_lazy("price")

    def form_valid(self, form):
        messages.success(self.request, "Цена была успешна удалена.")
        return super(PriceDelete, self).form_valid(form)

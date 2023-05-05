from django.urls import path
from . import views

urlpatterns = [
    path('', views.price_view, name="price"),
    # path('view/<int:pk>', views.PriceView.as_view(), name='price-view'),
    # path('delete/<int:pk>', views.PriceDelete.as_view(), name='price-delete'),
    # path('edit/<int:pk>', views.PriceUpdate.as_view(), name='price-edit'),
    # path('create/', views.PriceCreate.as_view(), name='create-price'),
]

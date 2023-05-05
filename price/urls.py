from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_price, name="price"),
    path('view/<int:pk>', views.detail_view_price, name='price-view'),
    path('delete/<int:pk>', views.delete_price, name='price-delete'),
    path('edit/<int:pk>', views.edit_price, name='price-edit'),
    path('create/', views.add_price, name='create-price'),
]

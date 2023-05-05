from django.urls import path
from . import views

urlpatterns = [
    path('', views.price_view, name="price"),
    # path('view_game/<int:pk>', views.PriceView.as_view(), name='price-view_game'),
    # path('delete_game/<int:pk>', views.PriceDelete.as_view(), name='price-delete_game'),
    # path('edit_game/<int:pk>', views.PriceUpdate.as_view(), name='price-edit_game'),
    # path('create/', views.PriceCreate.as_view(), name='create-price'),
]

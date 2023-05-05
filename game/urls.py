from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_game, name="game"),
    path('view_game/<int:pk>', views.detail_view_game, name='game-view'),
    path('delete_game/<int:pk>', views.delete_game, name='game-delete'),
    path('edit_game/<int:pk>', views.edit_game, name='game-edit'),
    path('create/', views.add_game, name='create-game'),
]

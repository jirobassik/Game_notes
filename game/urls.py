from django.urls import path
from . import views
from genre.views import *

urlpatterns = [
    path('', views.view_game, name="game"),
    path('view_game/<int:pk>', views.detail_view_game, name='game-view'),
    path('delete_game/<int:pk>', views.delete_game, name='game-delete'),
    path('edit_game/<int:pk>', views.edit_game, name='game-edit'),
    path('create/', views.add_game, name='create-game'),

    path('genre/', view_genres, name='genre_view_game'),
    path('genre/view_genre/<int:pk>', detail_view_genres, name='genre_view_game_detail'),
    path('genre/delete/<int:pk>', delete_genre, name='genre_view_game_delete'),
    path('genre/edit/<int:pk>', edit_genre, name='genre_view_game_edit'),
    path('genre/create/', add_genre, name='genre_view_game_create'),

]

from django.urls import path
from . import views
from game.views import view_game

urlpatterns = [
    path('', views.view_genres, name="genre"),
    # path('view_game/<int:pk>', views.GenreView.as_view(), name='genre-view_game'),
    path('delete_game/<int:pk>', views.delete_genre, name='genre-delete_game'),
    # path('edit_game/<int:pk>', views.GenreUpdate.as_view(), name='genre-edit_game'),
    path('create/', views.add_genre, name='create-genre'),
]
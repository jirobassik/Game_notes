from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_genres, name="genre"),
    path('view_game/<int:pk>', views.detail_view_genres, name='genre-view'),
    path('delete/<int:pk>', views.delete_genre, name='genre-delete'),
    path('edit/<int:pk>', views.edit_genre, name='genre-edit'),
    path('create/', views.add_genre, name='create-genre'),
]

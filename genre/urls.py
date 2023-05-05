from django.urls import path
from . import views

urlpatterns = [
    path('', views.Genre.as_view(), name="genre"),
    path('view/<int:pk>', views.GenreView.as_view(), name='genre-view'),
    path('delete/<int:pk>', views.GenreDelete.as_view(), name='genre-delete'),
    path('edit/<int:pk>', views.GenreUpdate.as_view(), name='genre-edit'),
    path('create/', views.GenreCreate.as_view(), name='create-genre'),
]
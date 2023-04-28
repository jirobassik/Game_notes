from django.urls import path
from . import views

urlpatterns = [
    path('', views.Game.as_view(), name="game"),
    path('view/<int:pk>', views.GameView.as_view(), name='game-view'),
    path('delete/<int:pk>', views.GameDelete.as_view(), name='game-delete'),
    path('edit/<int:pk>', views.GameUpdate.as_view(), name='game-edit'),
    path('create/', views.GameCreate.as_view(), name='create-game'),
]
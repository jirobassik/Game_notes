from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name="game"),
    # path('view/<int:pk>', views.GameView.as_view(), name='game-view'),
    path('delete/<int:pk>', views.delete, name='game-delete'),
    # path('edit/<int:pk>', views.GameUpdate.as_view(), name='game-edit'),
    path('create/', views.add, name='create-game'),
]

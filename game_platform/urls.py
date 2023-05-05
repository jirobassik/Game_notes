from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_platform, name="platform"),
    # path('view_game/<int:pk>', views.GamePlatformView.as_view(), name='platform-view_game'),
    path('delete_game/<int:pk>', views.delete_platform, name='platform-delete_game'),
    # path('edit_game/<int:pk>', views.GamePlatformUpdate.as_view(), name='platform-edit_game'),
    # path('create/', views.GamePlatformCreate.as_view(), name='create-platform'),
]
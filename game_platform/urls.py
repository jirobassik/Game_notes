from django.urls import path
from . import views

urlpatterns = [
    path('', views.GamePlatform.as_view(), name="platform"),
    path('view/<int:pk>', views.GamePlatformView.as_view(), name='platform-view'),
    path('delete/<int:pk>', views.GamePlatformDelete.as_view(), name='platform-delete'),
    path('edit/<int:pk>', views.GamePlatformUpdate.as_view(), name='platform-edit'),
    path('create/', views.GamePlatformCreate.as_view(), name='create-platform'),
]
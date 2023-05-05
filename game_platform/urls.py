from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_platform, name="platform"),
    path('view/<int:pk>', views.detail_view_platform, name='platform-view'),
    path('delete/<int:pk>', views.delete_platform, name='platform-delete'),
    path('edit/<int:pk>', views.edit_platform, name='platform-edit'),
    path('create/', views.add_platform, name='create-platform'),
]
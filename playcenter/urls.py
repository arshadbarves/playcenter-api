from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameAPI.as_view(), name='games'),
    path('game/<int:pk>/', views.GameDetailAPI.as_view(), name='game'),
    path('games/<int:game_id>/images/', views.game_detail, name='game_detail'),
]

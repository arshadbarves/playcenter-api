from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import permissions
from .models import *
from .serializers import *

# Game API to get all games


class GameAPI(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = GameDetail.objects.all()
    serializer_class = GameListSerializer


# Game API to get specific game
class GameDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = GameDetail.objects.all()
    serializer_class = GameDetailsSerializer


# Get the image from the database
def game_detail(request, game_id):
    game = get_object_or_404(GameDetail, pk=game_id)

    game_images = game.game_image.all()
    game_spotlight_images = game.game_spotlight_image.all()

    return render(request, 'game_detail.html', {
        'game': game,
        'game_images': game_images,
        'game_spotlight_images': game_spotlight_images,
    })

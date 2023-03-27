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

import random
import string
from rest_framework import serializers
from .models import *

# Game Details Serializer


class GameDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDetail
        fields = '__all__'
        read_only_fields = ('game_id',)

    # Make the image name as different from the original name by the time of uploading and randomize the name
    def create(self, validated_data):
        game = GameDetail.objects.create(**validated_data)
        game.game_spotlight_image.name = game.game_name + 'game_spotlight_image' + timezone.now().strftime("%Y%m%d%H%M%S") + random.choice(
            string.ascii_letters) + '.jpg'
        game.game_image.name = game.game_name + 'game_image' + \
            timezone.now().strftime("%Y%m%d%H%M%S") + \
            random.choice(string.ascii_letters) + '.jpg'
        game.save()
        return game

# Game List Serializer


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDetail
        fields = ('game_id', 'game_name', 'game_description',
                  'game_spotlight_image', 'game_status')
        read_only_fields = ('game_id',)

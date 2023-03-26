from django.contrib import admin

from .models import *

# Display the list games in GameScreenShot model in admin panel with the following fields in the list view of the admin panel


class GameScreenshotAdmin(admin.ModelAdmin):
    list_display = ('game', 'image')

    class Meta:
        model = GameScreenshot, GameReview, GameTrailer


# Register your models here.
admin.site.register(GameDetail)

admin.site.register(GameScreenshot)

admin.site.register(GameReview)

admin.site.register(GameTrailer)

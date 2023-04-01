from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create storage instance for cloudinary
cloudinary_storage = MediaCloudinaryStorage()

# Game Details Model


class GameDetail(models.Model):
    GAME_PLATFORM_CHOICES = (
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('PlayStation', 'PlayStation'),
        ('Nintendo', 'Nintendo'),
        ('Android', 'Android'),
        ('iOS', 'iOS'),
        ('Other', 'Other'),
    )
    GAME_GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Arcade', 'Arcade'),
        ('Board', 'Board'),
        ('Card', 'Card'),
        ('Casino', 'Casino'),
        ('Educational', 'Educational'),
        ('Family', 'Family'),
        ('Music', 'Music'),
        ('Puzzle', 'Puzzle'),
        ('Racing', 'Racing'),
        ('Role-Playing', 'Role-Playing'),
        ('Shooter', 'Shooter'),
        ('Simulation', 'Simulation'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
        ('Trivia', 'Trivia'),
        ('Word', 'Word'),
        ('Other', 'Other'),
    )

    GAME_AGE_RATING_CHOICES = (
        ('3+', '3+'),
        ('7+', '7+'),
        ('12+', '12+'),
        ('16+', '16+'),
        ('18+', '18+'),
    )
    GAME_STATUS_CHOICES = (
        ('Coming Soon', 'Coming Soon'),
        ('Early Access', 'Early Access'),
        ('Released', 'Released'),
        ('Cancelled', 'Cancelled'),
        ('Beta', 'Beta'),
        ('Alpha', 'Alpha'),
        ('Demo', 'Demo'),
    )
    LANGUAGE_CHOICES = (
        ('English', 'English'),
        ('French', 'French'),
        ('German', 'German'),
        ('Spanish', 'Spanish'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('Korean', 'Korean'),
        ('Chinese', 'Chinese'),
        ('Russian', 'Russian'),
        ('Other', 'Other'),
    )

    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=100)
    game_short_description = models.CharField(max_length=1000, default='None')
    game_description = models.TextField()
    game_spotlight_image = models.ImageField(
        upload_to='game/images/game_spotlight_images', unique=True, storage=cloudinary_storage)
    # Mutiple images for a game
    game_image = models.ImageField(
        upload_to='game/images/game_images', unique=True, storage=cloudinary_storage)
    game_video = models.URLField(max_length=1000)
    game_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    game_rating = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    game_release_date = models.DateField()
    game_genre = models.CharField(
        max_length=100, choices=GAME_GENRE_CHOICES, default='Action')
    game_publisher = models.CharField(max_length=100)
    game_developer = models.CharField(max_length=100)
    game_platform = models.CharField(
        max_length=100, choices=GAME_PLATFORM_CHOICES, default='PC')
    game_language = models.CharField(
        max_length=100, choices=LANGUAGE_CHOICES, default='English')
    game_system_requirements = models.TextField()
    game_tags = models.CharField(max_length=1000, default='None')
    game_age_rating = models.CharField(
        max_length=100, choices=GAME_AGE_RATING_CHOICES, default='3+')
    game_link = models.URLField(max_length=1000)
    game_status = models.CharField(
        max_length=100, choices=GAME_STATUS_CHOICES, default='Coming Soon')
    game_size = models.CharField(max_length=100, default='None')
    game_created_date = models.DateTimeField(default=timezone.now)
    game_updated_date = models.DateTimeField(default=timezone.now)

    # update game and spotlight image in cloudinary when game details are deleted
    @receiver(pre_delete, sender='playcenter.GameDetail')
    def auto_delete_file_on_delete(sender, instance, **kwargs):
        cloudinary_storage.delete(instance.game_image.name)
        cloudinary_storage.delete(instance.game_spotlight_image.name)
        instance.game_image.delete(save=False)
        instance.game_spotlight_image.delete(save=False)

    # update game and spotlight image in cloudinary when game details are updated
    @ receiver(pre_save, sender='playcenter.GameDetail')
    def auto_delete_file_on_change(sender, instance, **kwargs):
        if not instance.pk:
            return False

        try:
            old_file = sender.objects.get(pk=instance.pk).game_image
            new_file = instance.game_image
            old_file2 = sender.objects.get(pk=instance.pk).game_spotlight_image
            new_file2 = instance.game_spotlight_image
            if not old_file == new_file:
                old_file.delete(save=False)
            if not old_file2 == new_file2:
                old_file2.delete(save=False)
        except sender.DoesNotExist:
            return False

    def __str__(self):
        return self.game_name

    class Meta:
        ordering = ['-game_created_date']

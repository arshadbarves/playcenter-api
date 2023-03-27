from django.db import models
from django.utils import timezone

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
    game_description = models.TextField()
    game_spotlight_image = models.ImageField(upload_to='game_images')
    # Mutiple images for a game
    game_image = models.ImageField(upload_to='game_images')
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
    game_created_date = models.DateTimeField(default=timezone.now)
    game_updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.game_name

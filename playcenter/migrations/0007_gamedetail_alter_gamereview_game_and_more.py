# Generated by Django 4.1.7 on 2023-03-26 17:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playcenter', '0006_rename_game_image_gamedetails_game_image2023032617103132773_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameDetail',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=100)),
                ('game_description', models.CharField(max_length=1000)),
                ('game_spotlight_image', models.ImageField(upload_to='game_images')),
                ('game_image', models.ImageField(upload_to='game_images')),
                ('game_video', models.URLField(max_length=1000)),
                ('game_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('game_rating', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('game_release_date', models.DateField()),
                ('game_genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Arcade', 'Arcade'), ('Board', 'Board'), ('Card', 'Card'), ('Casino', 'Casino'), ('Educational', 'Educational'), ('Family', 'Family'), ('Music', 'Music'), ('Puzzle', 'Puzzle'), ('Racing', 'Racing'), ('Role-Playing', 'Role-Playing'), ('Shooter', 'Shooter'), ('Simulation', 'Simulation'), ('Sports', 'Sports'), ('Strategy', 'Strategy'), ('Trivia', 'Trivia'), ('Word', 'Word'), ('Other', 'Other'), ('MMO', 'MMO'), ('MOBA', 'MOBA'), ('Roguelike', 'Roguelike')], default='Action', max_length=100)),
                ('game_publisher', models.CharField(max_length=100)),
                ('game_developer', models.CharField(max_length=100)),
                ('game_platform', models.CharField(choices=[('PC', 'PC'), ('Xbox', 'Xbox'), ('PlayStation', 'PlayStation'), ('Nintendo', 'Nintendo'), ('Android', 'Android'), ('iOS', 'iOS'), ('Other', 'Other')], default='PC', max_length=100)),
                ('game_language', models.CharField(max_length=100)),
                ('game_system_requirements', models.CharField(max_length=1000)),
                ('game_tags', models.CharField(default='None', max_length=1000)),
                ('game_age_rating', models.CharField(choices=[('3+', '3+'), ('7+', '7+'), ('12+', '12+'), ('16+', '16+'), ('18+', '18+')], default='3+', max_length=100)),
                ('game_link', models.URLField(max_length=1000)),
                ('game_status', models.CharField(choices=[('Coming Soon', 'Coming Soon'), ('Early Access', 'Early Access'), ('Released', 'Released'), ('Cancelled', 'Cancelled'), ('Beta', 'Beta'), ('Alpha', 'Alpha'), ('Demo', 'Demo')], default='Coming Soon', max_length=100)),
                ('game_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('game_updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playcenter.gamedetail'),
        ),
        migrations.AlterField(
            model_name='gamescreenshot',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playcenter.gamedetail'),
        ),
        migrations.AlterField(
            model_name='gametrailer',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playcenter.gamedetail'),
        ),
        migrations.DeleteModel(
            name='GameDetails',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playcenter', '0003_delete_developer_delete_gameagerating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetails',
            name='game_video',
            field=models.URLField(max_length=1000),
        ),
    ]

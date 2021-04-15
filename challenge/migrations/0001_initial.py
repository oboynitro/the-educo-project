# Generated by Django 3.1.5 on 2021-01-23 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b7573d41-f97c-4d66-bfed-7b2120f26f86'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('match_bonus', models.IntegerField(default=1)),
                ('answer_bonus', models.IntegerField(default=1)),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('match_winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_winner', to=settings.AUTH_USER_MODEL)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Challenge',
                'verbose_name_plural': 'Challenges',
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b7573d41-f97c-4d66-bfed-7b2120f26f86'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(default=1)),
                ('player1_point', models.SmallIntegerField(default=0)),
                ('player2_point', models.SmallIntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_round', to='challenge.game')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='round_question', to='quiz.question')),
            ],
            options={
                'verbose_name': 'Round',
                'verbose_name_plural': 'Rounds',
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
    ]

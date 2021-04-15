# Generated by Django 3.1.5 on 2021-01-23 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b7573d41-f97c-4d66-bfed-7b2120f26f86'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('tags', models.TextField(null=True)),
                ('vote_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('solution_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Discussion',
                'verbose_name_plural': 'Discussions',
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b7573d41-f97c-4d66-bfed-7b2120f26f86'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField(null=True)),
                ('vote_count', models.IntegerField(default=0)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution_discussion', to='discussion.discussion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solution',
                'verbose_name_plural': 'Solutions',
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SolutionVote',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b7573d41-f97c-4d66-bfed-7b2120f26f86'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vote_type', models.CharField(max_length=5)),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution_vote', to='discussion.solution')),
            ],
            options={
                'verbose_name': 'Solution Vote',
                'verbose_name_plural': 'Solution Votes',
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiscussionVote',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b7573d41-f97c-4d66-bfed-7b2120f26f86'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vote_type', models.CharField(max_length=5)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_vote', to='discussion.discussion')),
            ],
            options={
                'verbose_name': 'Discussion Vote',
                'verbose_name_plural': 'Discussion Votes',
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
    ]

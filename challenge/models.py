from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin
from quiz.models import Question

User = settings.AUTH_USER_MODEL


class Game(ModelMixin):
    description = models.CharField(max_length=255)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player1")
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player2")
    status = models.CharField(max_length=255)
    match_bonus = models.IntegerField(default=1)
    answer_bonus = models.IntegerField(default=1)
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    match_winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="match_winner")  # winner

    class Meta(ModelMixin.Meta):
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    def __str__(self) -> str:
        return str(self.id)


class Round(ModelMixin):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_round")
    number = models.IntegerField(default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="round_question")
    # 0 - no answer, 1 - correct answer, -1 - wrong answer
    player1_point = models.SmallIntegerField(default=0)
    player2_point = models.SmallIntegerField(default=0)

    class Meta(ModelMixin.Meta):
        verbose_name = "Round"
        verbose_name_plural = "Rounds"

    def __str__(self) -> str:
        return str(self.id)


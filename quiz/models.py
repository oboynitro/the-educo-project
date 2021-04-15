from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin

User = settings.AUTH_USER_MODEL


class Question(ModelMixin):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="question_author")
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255, null=True, blank=True)
    option2 = models.CharField(max_length=255, null=True, blank=True)
    option3 = models.CharField(max_length=255, null=True, blank=True)
    option4 = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255)

    class Meta(ModelMixin.Meta):
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self) -> str:
        return str(self.id)

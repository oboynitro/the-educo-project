from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin

User = settings.AUTH_USER_MODEL


class Discussion(ModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussion_user")
    question = models.CharField(max_length=255)
    description = models.TextField(null=True)
    tags = models.TextField(null=True)
    vote_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    solution_count = models.IntegerField(default=0)

    class Meta(ModelMixin.Meta):
        verbose_name = "Discussion"
        verbose_name_plural = "Discussions"

    def __str__(self) -> str:
        return str(self.question)


class DiscussionVote(ModelMixin):
    discussion = models.ForeignKey(Discussion, related_name="discussion_vote", on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=5)  # up or down

    class Meta(ModelMixin.Meta):
        verbose_name = "Discussion Vote"
        verbose_name_plural = "Discussion Votes"

    def __str__(self) -> str:
        return str(self.id)


class Solution(ModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solution_user")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="solution_discussion")
    body = models.TextField(null=True)
    vote_count = models.IntegerField(default=0)

    class Meta(ModelMixin.Meta):
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

    def __str__(self) -> str:
        return str(self.id)


class SolutionVote(ModelMixin):
    solution = models.ForeignKey(Solution, related_name="solution_vote", on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=5)  # up or down

    class Meta(ModelMixin.Meta):
        verbose_name = "Solution Vote"
        verbose_name_plural = "Solution Votes"

    def __str__(self) -> str:
        return str(self.id)

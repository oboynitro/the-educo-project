from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin

User = settings.AUTH_USER_MODEL


class Leaderboard(ModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leaderboard_user")
    points = models.IntegerField(default=0)
    position = models.IntegerField(default=1)

    class Meta(ModelMixin.Meta):
        verbose_name = "Leaderboard"
        verbose_name_plural = "Leaderboard"

    def __str__(self) -> str:
        return str(self.id)


class Notification(ModelMixin):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_sender")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_recipient")
    read = models.BooleanField(default=False)
    description = models.CharField(max_length=255)  # like | comment | challenge | vote
    activity_id = models.CharField(max_length=255)

    class Meta(ModelMixin.Meta):
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self) -> str:
        return str(self.id)

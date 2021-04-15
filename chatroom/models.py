from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin

User = settings.AUTH_USER_MODEL


class Message(ModelMixin):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_recipient")
    body = models.TextField()
    read = models.BooleanField(default=False)

    class Meta(ModelMixin.Meta):
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self) -> str:
        return str(self.id)

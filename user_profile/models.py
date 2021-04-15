from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin

User = settings.AUTH_USER_MODEL


class Profile(ModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    profile_image = models.ImageField()
    mobile = models.CharField(max_length=20, default="xxx-xxx-xxxx")
    location = models.CharField(max_length=255, null=True)
    level = models.IntegerField(default=1)

    class Meta(ModelMixin.Meta):
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return str(self.id)

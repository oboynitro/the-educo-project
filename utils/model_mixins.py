import uuid
from django.db import models


class ModelMixin(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at", "-created_at"]

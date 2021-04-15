from django.db import models
from django.conf import settings

from utils.model_mixins import ModelMixin

User = settings.AUTH_USER_MODEL


class Feed(ModelMixin):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feed_user")
    description = models.CharField(max_length=255, null=True, blank=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    class Meta(ModelMixin.Meta):
        verbose_name = "Activity Feed"
        verbose_name_plural = "Activities Feed"

    def __str__(self) -> str:
        return str(self.id)


class FeedLike(ModelMixin):
    feed = models.ForeignKey(Feed, related_name="feed_likes", on_delete=models.CASCADE)

    class Meta(ModelMixin.Meta):
        verbose_name = "Feed like"
        verbose_name_plural = "Feed likes"

    def __str__(self) -> str:
        return str(self.id)


class FeedFile(ModelMixin):
    feed = models.ForeignKey(Feed, related_name="feed_files", on_delete=models.CASCADE)
    file_type = models.CharField(max_length=255)
    file_link = models.CharField(max_length=255)

    class Meta(ModelMixin.Meta):
        verbose_name = "Feed file"
        verbose_name_plural = "Feed files"

    def __str__(self) -> str:
        return str(self.id)


class Comment(ModelMixin):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="feed_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    body = models.TextField()
    like_count = models.IntegerField(default=0)

    class Meta(ModelMixin.Meta):
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return str(self.id)


class CommentLike(ModelMixin):
    comment = models.ForeignKey(Comment, related_name="comment_likes", on_delete=models.CASCADE)

    class Meta(ModelMixin.Meta):
        verbose_name = "Comment like"
        verbose_name_plural = "Comment likes"

    def __str__(self) -> str:
        return str(self.id)


class CommentFile(ModelMixin):
    comment = models.ForeignKey(Comment, related_name="comment_files", on_delete=models.CASCADE)
    file_type = models.CharField(max_length=255)
    file_link = models.CharField(max_length=255)

    class Meta(ModelMixin.Meta):
        verbose_name = "Comment file"
        verbose_name_plural = "Comment files"

    def __str__(self) -> str:
        return str(self.id)

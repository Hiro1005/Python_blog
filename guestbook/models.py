from django.db import models
from django.utils.timezone import now


class Greeting(models.Model):

    """コメント."""

    name = models.CharField(verbose_name='名前', max_length=100,
                            blank=False, null=False)
    comment = models.TextField(verbose_name='コメント')
    created_at = models.DateTimeField(verbose_name='投稿日時', default=now)

    class Meta:
        db_table = "greeting"

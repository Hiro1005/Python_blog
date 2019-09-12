from django.db import models
from django.utils.timezone import now


class Greeting(models.Model):

    """コメント."""

    name = models.CharField(verbose_name='Name', max_length=100,
                            blank=False, null=False)
    comment = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(verbose_name='投稿日時', default=now)

    class Meta:
        db_table = "greeting"

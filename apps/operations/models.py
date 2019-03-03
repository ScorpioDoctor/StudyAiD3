from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from blogs.models import Article

User = get_user_model()


class UserFavor(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="文章", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")

    def __str__(self):
        return self.user.username

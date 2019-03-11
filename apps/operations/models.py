from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from blogs.models import Article, Album

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


class AlbumFavor(models.Model):
    """
    专辑收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    album = models.ForeignKey(Album, verbose_name="专辑", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '专辑收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "album")

    def __str__(self):
        return self.user.username + ' : ' + self.album.name


class UserMessage(models.Model):
    """
    用户消息
    """
    user = models.ForeignKey(User, related_name='user', verbose_name="发消息用户", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='reciever', verbose_name="收消息用户", on_delete=models.CASCADE)
    message = models.TextField(default="", verbose_name="消息内容", help_text="消息内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

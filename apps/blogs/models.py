from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

from DjangoUeditor.models import UEditorField
from taxonomies.models import FirstCategory, SecondCategory, Tag, get_sentinel_category1, get_sentinel_category2

User = get_user_model()


# 某个作者被删除的时候该作者对应的所有文章都将会放到 'DeletedUser' 这个用户名下面
def get_sentinel_user():
    return User.objects.get_or_create(username='DeletedUser')[0]


class Album(models.Model):
    category1 = models.ForeignKey(FirstCategory, verbose_name="一级类别", on_delete=models.SET(get_sentinel_category1))
    category2 = models.ForeignKey(SecondCategory, verbose_name="二级类别", on_delete=models.SET(get_sentinel_category2))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="文集标签")
    user = models.ForeignKey(User, verbose_name='文集作者', on_delete=models.SET(get_sentinel_user)) # 给外键设置默认值
    name = models.CharField(max_length=255, verbose_name='文集名称')
    brief = models.CharField(max_length=120, verbose_name='文集简介', default='这个文集暂无简介', blank=True)
    cover = models.ImageField(upload_to='albums/images/', verbose_name='文集封面', max_length=255, null=True, blank=True)
    click_num = models.IntegerField(verbose_name='点击量', default=0)
    focus_num = models.IntegerField(verbose_name='关注量', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文集'
        verbose_name_plural = verbose_name


class Article(models.Model):
    category1 = models.ForeignKey(FirstCategory, verbose_name="一级类别", on_delete=models.SET(get_sentinel_category1))
    category2 = models.ForeignKey(SecondCategory, verbose_name="二级类别", on_delete=models.SET(get_sentinel_category2))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="文章标签")
    user = models.ForeignKey(User, verbose_name='文章作者', on_delete=models.SET(get_sentinel_user)) # 给外键设置默认值
    album = models.ForeignKey(Album, verbose_name='所属文集', on_delete=models.CASCADE) # 级联删除
    title = models.CharField(max_length=255, verbose_name='文章标题')
    brief = models.CharField(max_length=120, verbose_name='文章摘要', default='这篇文章没有摘要', blank=True)
    cover = models.ImageField(upload_to='articles/images/', verbose_name='文章封面', max_length=255, null=True, blank=True)
    # content = models.TextField(verbose_name='文章内容')
    content = UEditorField(verbose_name='文章内容', width=800, height=500, toolbars="full",
                           imagePath="articles/images/", filePath="articles/files/", blank=True, default="")
    click_num = models.IntegerField(verbose_name='点击量', default=0)
    favor_num = models.IntegerField(verbose_name='收藏量', default=0)
    comment_num = models.IntegerField(verbose_name='评论量', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name



from datetime import datetime

from django.db import models


class FirstCategory(models.Model):
    """
    一级分类类目
    """
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "一级类目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 某个类别被删除的时候该类别对应的所有实体都将会放到 'DeletedCategory' 这个类别下面
def get_sentinel_category1():
    return FirstCategory.objects.get_or_create(name='DeletedCategory1')[0]


class SecondCategory(models.Model):
    """
    二级分类类目
    """
    parent = models.ForeignKey(FirstCategory, verbose_name="父类目", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "二级类目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 某个类别被删除的时候该类别对应的所有实体都将会放到 'DeletedCategory2' 这个类别下面
def get_sentinel_category2():
    return SecondCategory.objects.get_or_create(name='DeletedCategory2')[0]


class Tag(models.Model):
    """
    分类标签
    """
    category1 = models.ForeignKey(FirstCategory, verbose_name="标签类别", on_delete=models.SET(get_sentinel_category1))
    name = models.CharField(max_length=25, verbose_name='标签名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类标签'
        verbose_name_plural = verbose_name

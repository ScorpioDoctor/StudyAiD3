# Generated by Django 2.0.5 on 2019-03-07 17:36

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import taxonomies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxonomies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='文集名称')),
                ('brief', models.CharField(blank=True, default='这个文集暂无简介', max_length=120, verbose_name='文集简介')),
                ('cover', models.ImageField(blank=True, default='albums/images/albumcover.png', max_length=255, null=True, upload_to='albums/images/', verbose_name='文集封面')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('focus_num', models.IntegerField(default=0, verbose_name='关注量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文集',
                'verbose_name_plural': '文集',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='文章标题')),
                ('brief', models.CharField(blank=True, default='这篇文章没有摘要', max_length=120, verbose_name='文章摘要')),
                ('cover', models.ImageField(blank=True, max_length=255, null=True, upload_to='articles/images/', verbose_name='文章封面')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章内容')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('favor_num', models.IntegerField(default=0, verbose_name='收藏量')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Album', verbose_name='所属文集')),
                ('category1', models.ForeignKey(on_delete=models.SET(taxonomies.models.get_sentinel_category1), to='taxonomies.FirstCategory', verbose_name='一级类别')),
                ('category2', models.ForeignKey(on_delete=models.SET(taxonomies.models.get_sentinel_category2), to='taxonomies.SecondCategory', verbose_name='二级类别')),
                ('tags', models.ManyToManyField(blank=True, to='taxonomies.Tag', verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
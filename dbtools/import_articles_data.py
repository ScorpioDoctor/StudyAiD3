# -*- coding: utf-8 -*-

__author__ = 'antares'
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudyAiD4.settings")

import django
from django.contrib.auth import get_user_model

django.setup()

from random import randint, choice

from taxonomies.models import FirstCategory, SecondCategory, Tag
from blogs.models import Article, Album


def get_random_str(orig_str, maxLength=-1):
    length = len(orig_str)
    half = int(length / 2)
    if maxLength == -1:
        return orig_str[randint(0, half): randint(half, length)]
    else:
        temp_str = orig_str[randint(0, half): randint(half, length)]
        returnLength = min(len(temp_str), maxLength)
        return temp_str[0: returnLength]


titles_str = "普通最小二乘法流形学习聚类分析PCA朴素贝叶斯高斯过程支持向量机DBSCANKMEANS变分法核密度估计12月到一月期间我在印度闲逛了一个月上至喜马拉雅山脚下至阿拉伯海岸也算是跋山涉水走南闯北这是个如此丰富的国家每一张脸上的每一个表情每一条巷道中的每一块砖瓦每一座庙宇里的每一个飞檐每一样美食里的每一种香料每一首歌谣里的每一个和声背后都有一本书也写不完的故事作为游客一个月的时间甚至不能算触及了皮毛但我想即使这些流于表面的浮光掠影拍案惊奇对于一个远远未被世人所认识甚至背负着太多误解的国家来说多少也有存在的价值"
brief_str = "科钦所属的卡拉拉邦自1957年建邦至今的大部分时间里，一直都是共产党执政，虽然选举产生的坐庄党派时有交替，但这些党派大都是共产党衍生出来的自家兄弟。今天，作为资本主义印度的唯一一个共产党执政邦，卡拉拉以全国最高的受教育程度（文盲只占6%），最高平均寿命（74岁）和第二低贫困率（7.05%) 傲视群雄，这里的人对他们执政党的感激是发自内心的假设你有一个包含数百个特征（变量）的数据集，却对数据所属的领域几乎没有什么了解。你需要去识别数据中的隐藏模式，探索和分析数据集。不仅如此，你还必须找出数据中是否存在模式－－用以判定数据是有用信号还是噪音"
alphabet_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
desc_str = """
<h1 class="ql-align-center">
                      <span class="ql-font-serif" style="background-color: rgb(240, 102, 102); color: rgb(255, 255, 255);"> I am Example 1! </span>
                    </h1>
                    <p><br></p>
                    <p><span class="ql-font-serif">W Can a man still be brave if he's afraid? That is the only time a man can be brave. </span></p>
                    <p><br></p>
                    <p><strong class="ql-font-serif ql-size-large">Courage and folly is </strong><strong class="ql-font-serif ql-size-large" style="color: rgb(230, 0, 0);">always</strong><strong class="ql-font-serif ql-size-large"> just a fine line.</strong></p>
                    <p><br></p>
                    <p><u class="ql-font-serif">There is only one God, and his name is Death. And there is only one thing we say to Death: "Not today."</u></p>
                    <p><br></p>
                    <p><em class="ql-font-serif">Fear cuts deeper than swords.</em></p>
                    <p><br></p>
                    <pre class="ql-syntax" spellcheck="false">const a = 10;<br>const editorOption = { highlight: text => hljs.highlightAuto(text).value };</pre>
                    <p><br></p>
                    <p><span class="ql-font-serif">Every flight begins with a fall.</span></p>
                    <p><br></p>
                    <p><a href="https://surmon.me/" target="_blank" class="ql-font-serif ql-size-small" style="color: rgb(230, 0, 0);"><u>A ruler who hides behind paid executioners soon forgets what death is. </u></a></p>
                    <p><br></p>
                    <iframe class="ql-video ql-align-center" frameborder="0" allowfullscreen="true" src="http://724.169pp.net/bizhi/2017/042/2.jpg" width="800" height="1000"></iframe>
                    <p><br></p>
                    <p><span class="ql-font-serif">Hear my words, and bear witness to my vow. Night gathers, and now my watch begins. It shall not end until my death. I shall take no wife, hold no lands, father no children. I shall wear no crowns and win no glory. I shall live and die at my post. I am the sword in the darkness. I am the watcher on the walls. I am the fire that burns against the cold, the light that brings the dawn, the horn that wakes the sleepers, the shield that guards the realms of men. I pledge my life and honor to the Night’s Watch, for this night and all the nights to come.</span></p>
                    <p><br></p>
                    <p><span class="ql-font-serif">We are born to suffer, to suffer can make us strong.</span></p>
                    <p><br></p>
                    <p><span class="ql-font-serif">The things we love destroy us every time.</span></p>
                    <p><br></p>
                    <iframe height=480 width=640 src='http://player.youku.com/embed/XMzc5NTczMzcwNA==' class="ql-video ql-align-center" frameborder="0" allowfullscreen="true" ></iframe>                        <p><br></p>
"""

# 拿到所有的标签
tags = Tag.objects.filter()

# 拿到所有的用户
User = get_user_model()

covers = [str(x) + '.png' for x in range(1, 20)]


# 生成一篇文章
def GenerateOneFakeData():
    art = Article()
    art.title = get_random_str(titles_str, 20)
    art.brief = get_random_str(brief_str, 120)
    art.content = desc_str
    art.click_num = randint(10, 100)
    art.favor_num = randint(10, 100)
    art.comment_num = randint(10, 100)
    art.cover = "articles/images/" + choice(covers)
    # 指定当前文章的用户
    art.user = choice(User.objects.all())
    # 把当前文章指定到这个用户的某个文集
    art.album = choice(Album.objects.filter(user=art.user))

    # 当前文章的类别
    art.category1 = art.album.category1
    art.category2 = art.album.category2
    # 为当前文章指定若干tags
    # art.tags.set(ArticleTag(name=tags[randint(0,tags.count()-1)].name))
    # art.user = choice(User.objects.all())  # 随机选择一个用户
    # category1 = choice(FirstCategory.objects.all())  # 随机选择一个一级类目
    # category2 = choice(SecondCategory.objects.filter(parent=category1))  # 在一级类目下随机选择二级类目
    # art.category1 = category1
    # art.category2 = category2
    return art


for _ in range(1000):
    art = GenerateOneFakeData()
    print('==' * 30)
    print('title: ', art.title)
    print('brief: ', art.brief)
    print('cover: ', art.cover)
    print('favor: ', art.favor_num)
    print('click: ', art.click_num)
    print('cat-1: ', art.category1)
    print('cat-2: ', art.category2)
    print('user: ', art.user)
    art.save()
    # art.tags.set(tags[0:2])

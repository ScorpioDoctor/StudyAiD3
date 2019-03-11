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

from users.models import UserProfile

User = get_user_model()

from blogs.models import Album
from taxonomies.models import FirstCategory, SecondCategory, Tag

from random import randint, choice


def get_random_str(orig_str, maxLength=-1):
    length = len(orig_str)
    half = int(length / 2)
    if maxLength == -1:
        return orig_str[randint(0, half): randint(half, length)]
    else:
        temp_str = orig_str[randint(0, half): randint(half, length)]
        returnLength = min(len(temp_str), maxLength)
        return temp_str[0: returnLength]


titles_str = ['冰川思想库', '聊斋志异', '唐诗宋词', '谈美书简', 'ToFEL词汇', '水花转', 'NodeJS实战', 'VueJS实战',
              'Python实战', '玩坏TensorFlow', '黑瞳专辑', '黑洞探秘', '人体工学', '自控原理', '模拟电路', '数字逻辑',
              '离散数学', '高斯其人', '莱布尼茨大揭秘', '爱因斯坦很聪明', '牛顿是个什么人', '一带一路面面观']
brief_str = '套用于构建用户界面的渐进式框架与其它大型框架不同的是被设计为可以自底向上逐层应用的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。'

covers = [str(x) + '.png' for x in range(1, 20)]

#
for _ in range(300):
    album = Album()
    album.name = choice(titles_str) + get_random_str('abcdefghijklmnopqrstuvwxyz1234567890', 6)
    album.brief = get_random_str(brief_str, 100)
    album.click_num = randint(10, 200)
    album.focus_num = randint(50, 100)
    album.cover = 'albums/images/' + choice(covers)
    album.user = choice(User.objects.all())  # 随机选择一个用户
    category1 = choice(FirstCategory.objects.all())  # 随机选择一个一级类目
    category2 = choice(SecondCategory.objects.filter(parent=category1))  # 在一级类目下随机选择二级类目
    album.category1 = category1
    album.category2 = category2
    print('name: ', album.name)
    print('click: ', album.click_num)
    print('brief: ', album.brief)
    print('user: ', album.user.username)
    print('cat-1: ', album.category1)
    print('cat-2: ', album.category2)
    # print('tags: ', album.tags)
    album.save()

# 设置 tags
# albums = Album.objects.all()
# for album in albums:
#     tags = Tag.objects.filter(category1=album.category1, category2=album.category2)
#     print(tags)
#     if len(tags) > 0:
#         album.tags.set(tags[0:randint(1,3)])
#         pass


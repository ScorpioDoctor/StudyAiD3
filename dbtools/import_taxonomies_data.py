# -*- coding: utf-8 -*-
__author__ = 'antares'

# 独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudyAiD4.settings")

import django

django.setup()

from taxonomies.models import FirstCategory, SecondCategory, Tag

tags_data = ['python', 'java', 'nodejs', 'javascript', 'html', 'css', 'julia', 'matlab', 'go', 'c++', 'linux', 'mysql',
             'mongodb', 'vue', 'react', 'django', 'flask', 'tornado', 'latex', 'word', 'pyramid', 'excel', 'bigdata']
#
# for tag_name in tags_data:
#     tag = Tag()
#     tag.name = tag_name
#     tag.save()
#     print(tag.id, ' ---> ', tag.name)

categories_data = {
    # '机器学习': ['ML基础', 'ML前沿', 'SKLearn', 'MATLAB-ML', 'R语言'],
    # '机器视觉': ['CV基础', 'CV前沿', 'OpenCV', 'MATLAB-CV', 'Scikit-Image','PyTorch-CV', 'TensorFlow-CV'],
    # '自然语言':  ['NLP基础', 'NLP前沿', 'NLTK', 'MATLAB-NLP', 'PyTorch-NLP', 'TensorFlow-NLP'],
    # '语音识别': ['SR基础', 'SR前沿', 'WaveAudio', 'MATLAB-SR', 'PyTorch-SR', 'TensorFlow-SR'],
    # '机器人': ["ROS系统", "无人驾驶"],
    # '大数据': ["交通大数据", "海洋大数据", "Hadoop", "Storm", "SPARK"],
    # '量化交易': ["QT基础", "QT研究", "京东金融", "蚂蚁金服", "同花顺", "米筐"],
    # '物联网': ["5G通信", "车联网", "家电网", "网络协议"],
    '个人中心':["我的信息", "我的专辑", "我的文章", "我的收藏", "我的消息"]
}

# 顶部导航栏的一级分类和侧边栏的二级分类
for cat1, cat2s in categories_data.items():
    fc = FirstCategory()
    fc.name = cat1
    fc.save()
    for cat2 in cat2s:
        sc = SecondCategory()
        sc.parent = fc
        sc.name = cat2
        sc.save()
        print(fc, ' ---> ', sc)

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

from random import randint


def get_random_str(orig_str, maxLength=-1):
    length = len(orig_str)
    half = int(length / 2)
    if maxLength == -1:
        return orig_str[randint(0, half): randint(half, length)]
    else:
        temp_str = orig_str[randint(0, half): randint(half, length)]
        returnLength = min(len(temp_str), maxLength)
        return temp_str[0: returnLength]


alphabet_str = 'abcdefghijklmnopqrstuvwxyz0123456789'


def GenerateOneFakeData():
    user = User()
    user.username = get_random_str(alphabet_str, 8)
    user.nickname = user.username
    user.email = get_random_str(alphabet_str, 8) + '@qq.com'
    user.set_password('qazwsx123')
    return user


for _ in range(10):
    user = GenerateOneFakeData()
    user.save()
    print(user.username)
    print(user.password)

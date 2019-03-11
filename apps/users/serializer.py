import re
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from StudyAiD4.settings import REGEX_MOBILE
from .models import UserProfile, VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'nickname', 'username')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'nickname', 'email', 'mobile')


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={ "blank": "请输入验证码", "required": "验证码是必填项", },
                                 help_text="验证码")
    nickname = serializers.CharField(label="昵称", help_text="昵称", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="昵称已经存在")])

    mobile = serializers.CharField(label="手机号", help_text="手机号", required=True, allow_blank=False,
                                   max_length=11, min_length=11,
                                   validators=[UniqueValidator(queryset=User.objects.all(), message="手机号已经存在")])

    password = serializers.CharField(style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True)

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["mobile"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["username"] = attrs["nickname"]
        del attrs["code"]
        # attrs["password"] = make_password(attrs["password"])
        return attrs

    class Meta:
        model = User
        fields = ("nickname", "mobile", "code", "password")

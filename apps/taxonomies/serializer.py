from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import FirstCategory, SecondCategory, Tag


class FirstCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstCategory
        fields = ('id', 'name')


class SecondCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondCategory
        fields = ('id', 'name', 'parent')


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="标签名", help_text="标签名", required=True, allow_blank=False, max_length=32,
                                     validators=[UniqueValidator(queryset=Tag.objects.all(), message="标签名已经存在")])
    class Meta:
        model = Tag
        fields = ('name', 'id')

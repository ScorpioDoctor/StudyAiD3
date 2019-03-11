from rest_framework import serializers

from taxonomies.models import Tag
from taxonomies.serializer import FirstCategorySerializer, SecondCategorySerializer, TagSerializer
from users.serializer import UserShowSerializer
from .models import Album, Article


class AlbumSerializer(serializers.ModelSerializer):
    category1 = FirstCategorySerializer()
    category2 = SecondCategorySerializer()
    user = UserShowSerializer()

    class Meta:
        model = Album
        fields = '__all__'


class AlbumSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name')


class AlbumCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Album
        fields = ('name', 'brief', 'cover', 'user', 'category1', 'category2', 'tags', 'id')


class ArticleSerializer(serializers.ModelSerializer):
    category1 = FirstCategorySerializer()
    category2 = SecondCategorySerializer()
    user = UserShowSerializer()
    album = AlbumSimpleSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Article
        fields = ('title', 'brief', 'cover', 'content', 'user', 'album', 'category1', 'category2', 'tags', 'id')

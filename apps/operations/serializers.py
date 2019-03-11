from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from blogs.serializer import ArticleSerializer, AlbumSerializer
from users.serializer import UserShowSerializer
from .models import UserFavor, AlbumFavor, UserMessage


class UserFavorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFavor
        fields = ('user', 'article', 'id')
        validators = [
            UniqueTogetherValidator(queryset=UserFavor.objects.all(),
                                    fields=('user', 'article'), message='已经收藏过了')
        ]


class UserFavorDetailSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = UserFavor
        fields = ('user', 'article', 'id')


class AlbumFavorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AlbumFavor
        fields = ('user', 'album', 'id')
        validators = [
            UniqueTogetherValidator(queryset=AlbumFavor.objects.all(),
                                    fields=('user', 'album'), message='已经收藏过了')]


class AlbumFavorDetailSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = AlbumFavor
        fields = ('user', 'album', 'id')


class UserMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserMessage
        fields = ('user', 'reciever', 'message', 'id')

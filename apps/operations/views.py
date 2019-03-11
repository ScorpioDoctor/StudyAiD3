from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .models import UserFavor, AlbumFavor, UserMessage
from .serializers import UserFavorSerializer, UserFavorDetailSerializer, AlbumFavorSerializer, \
    AlbumFavorDetailSerializer, UserMessageSerializer


class UserFavorViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户收藏文章功能
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'article_id'

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavorDetailSerializer
        if self.action == "retrieve":
            return UserFavorSerializer
        if self.action == 'create':
            return UserFavorSerializer
        return UserFavorSerializer

    def get_queryset(self):
        return UserFavor.objects.filter(user=self.request.user)


class AlbumFavorViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户收藏专辑功能
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'album_id'

    def get_serializer_class(self):
        if self.action == "list":
            return AlbumFavorDetailSerializer
        if self.action == "retrieve":
            return AlbumFavorSerializer
        if self.action == 'create':
            return AlbumFavorSerializer
        return AlbumFavorSerializer

    def get_queryset(self):
        return AlbumFavor.objects.filter(user=self.request.user)


class UserMessageViewset(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserMessageSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'user_id'

    def get_queryset(self):
        return UserMessage.objects.filter(user=self.request.user)

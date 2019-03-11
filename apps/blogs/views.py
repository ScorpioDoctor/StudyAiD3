from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters, authentication, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Album, Article
from .serializer import AlbumSerializer, ArticleSerializer, AlbumCreateSerializer, ArticleCreateSerializer


class BlogsPagination(PageNumberPagination):
    """
    自定义文章和专辑列表分页器
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 300


class AlbumListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    专集列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = BlogsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('category1', 'category2', 'tags', 'user_id')
    search_fields = ('name', 'brief',)
    ordering_fields = ('click_num', 'focus_num', 'add_time')


class AlbumCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    文集 创建，
    """
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class ArticleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    文章列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = BlogsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('category1', 'category2', 'tags', 'album', 'user')
    search_fields = ('title', 'brief', 'content')
    ordering_fields = ('click_num', 'favor_num', 'add_time')


class ArticleCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    文章 创建，
    """
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

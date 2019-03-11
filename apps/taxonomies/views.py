from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from .models import FirstCategory, SecondCategory, Tag
from .serializer import FirstCategorySerializer, SecondCategorySerializer, TagSerializer


class FirstCategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    一级分类类目列表
    """
    queryset = FirstCategory.objects.all()
    serializer_class = FirstCategorySerializer


class SecondCategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    二级分类类目列表
    """
    queryset = SecondCategory.objects.all()
    serializer_class = SecondCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('parent',)


class TagsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    标签分类类目 list,retrieve, create
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

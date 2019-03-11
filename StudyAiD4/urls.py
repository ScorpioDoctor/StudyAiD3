"""StudyAiD4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from StudyAiD4.settings import MEDIA_ROOT
from taxonomies import views as taxonomies_views
from users import views as user_views
from blogs import views as blogs_vies
from operations import views as operate_views


router = DefaultRouter()

# 分类系统相关的路由
router.register('categories1', taxonomies_views.FirstCategoryListViewSet, base_name='categories1')
router.register('categories2', taxonomies_views.SecondCategoryListViewSet, base_name='categories2')
router.register('tags', taxonomies_views.TagsViewSet, base_name='tags')

# 用户相关路由
router.register('codes', user_views.SmsCodeViewset, base_name='codes')
router.register('regist', user_views.UserRegViewset, base_name='regist')
router.register('users', user_views.UsersViewset, base_name='users')

# 博客系统相关路由
router.register('albums', blogs_vies.AlbumListViewSet, base_name='albums')
router.register('albumcreate', blogs_vies.AlbumCreateViewSet, base_name='albumcreate')
router.register('articles', blogs_vies.ArticleListViewSet, base_name='articles')
router.register('articlecreate', blogs_vies.ArticleCreateViewSet, base_name='articlecreate')

# 用户操作相关路由
router.register('userfavor', operate_views.UserFavorViewset, base_name='userfavor')
router.register('albumfavor', operate_views.AlbumFavorViewset, base_name='albumfavor')
router.register('usermessage', operate_views.UserMessageViewset, base_name='usermessage')


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # drf 文档
    re_path(r'^docs/', include_docs_urls(title='人工智能社区')),
    # api 认证
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # drf token 认证
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    # JWT token 认证
    re_path(r'^login/', obtain_jwt_token),
    # 路由集合
    path('', include(router.urls)),
]

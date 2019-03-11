# encoding: utf-8

import xadmin
from xadmin import views
from .models import VerifyCode, UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "人工智能社区后台"
    site_footer = "studyai"
    # menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ['username', 'nickname', 'mobile', 'email', "add_time"]
    search_fields = ['username', 'nickname', 'mobile', 'email']


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

import xadmin
from .models import UserFavor


class UserFavorAdmin(object):
    list_display = ["user", "article", "add_time"]
    list_filter = ["user", "article", "add_time"]


xadmin.site.register(UserFavor, UserFavorAdmin)

import xadmin
from .models import UserFavor, AlbumFavor, UserMessage


class UserFavorAdmin(object):
    list_display = ["id", "user", "article", "add_time"]
    list_filter = ["user", "article", "add_time"]


class AlbumFavorAdmin(object):
    list_display = ["id", "user", "album", "add_time"]
    list_filter = ["user", "album", "add_time"]


class UserMessageAdmin(object):
    list_display = ["id", "user", "reciever", "message", "add_time"]
    list_filter = ["user", "reciever", "add_time"]


xadmin.site.register(UserFavor, UserFavorAdmin)
xadmin.site.register(AlbumFavor, AlbumFavorAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)

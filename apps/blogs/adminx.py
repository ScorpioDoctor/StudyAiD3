import xadmin
from .models import Article, Album


class AlbumAdmin(object):
    list_display = ["name", "category1", "category2", "user", "click_num", "focus_num", "add_time"]
    search_fields = ['name', 'brief']
    list_editable = ['name', "category1", "category2", "click_num", "focus_num"]
    list_filter = ["category1", "category2", "click_num", "focus_num", "add_time"]


class ArticleAdmin(object):
    list_display = ["title", "category1", "category2", "user", "album", "click_num", "favor_num", "comment_num",
                    "add_time"]
    search_fields = ['title', 'brief']
    list_editable = ['title', "category1", "category2", "album", "click_num", "comment_num", "favor_num"]
    list_filter = ["category1", "category2", "album", "click_num", "comment_num", "favor_num", "add_time"]
    style_fields = {"content": "ueditor"}


xadmin.site.register(Album, AlbumAdmin)
xadmin.site.register(Article, ArticleAdmin)

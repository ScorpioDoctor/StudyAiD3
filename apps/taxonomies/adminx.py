import xadmin
from .models import FirstCategory, SecondCategory, Tag


class FirstCategoryAdmin(object):
    list_display = ["name", "add_time"]
    list_filter = ["add_time", ]
    search_fields = ['name', ]


class SecondCategoryAdmin(object):
    list_display = ["name", "parent", "add_time"]
    list_filter = ["parent", "add_time", ]
    search_fields = ['name', ]


class TagAdmin(object):
    list_display = ["name", "category1", "category2", "add_time"]
    list_filter = ["category1", "category2", "add_time", ]
    search_fields = ['name', ]


xadmin.site.register(FirstCategory, FirstCategoryAdmin)
xadmin.site.register(SecondCategory, SecondCategoryAdmin)
xadmin.site.register(Tag, TagAdmin)

from django.contrib import admin

from .models import *


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class TipAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Tip, TipAdmin)
admin.site.register(Comment)
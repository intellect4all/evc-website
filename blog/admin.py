from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "status")
    list_filter = ("published", "author")
    search_fields = ("title", "content")


admin.site.register(models.Category)
admin.site.register(models.Tag)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "content", "allowed")
    list_filter = ("name", "content", "allowed")
    search_fields = ("name", "content", "subject")

# Register your models here.

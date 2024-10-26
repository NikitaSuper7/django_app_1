from django.contrib import admin
from .models import BlogPostsModel
# Register your models here.

@admin.register(BlogPostsModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "text", "image", "created_at", "updated_at",
                    "is_publicated", "views_counter")
    list_filter = ("is_publicated", "views_counter", "created_at")
    search_fields = ("title", "text")


from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "price", "category", 'image', 'videos')
    list_filter = ("category",)
    search_fields = ("name", "description",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name",)
    search_fields = ("name", "category_description",)

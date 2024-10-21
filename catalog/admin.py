from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", 'image')
    list_filter = ("category",)
    search_fields = ("name", "description",)
    delete_confirmation_template = True
    delete_selected_confirmation_template = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name",)
    search_fields = ("name", "category_description",)

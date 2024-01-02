from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_enabled", "parent")
    list_filter = ("parent", "is_enabled")
    search_fields = ("title",)


class FileInline(admin.StackedInline):
    model = File
    fields = ("title", "file", "is_enable")
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "is_enable")
    list_filter = ("title", "is_enable")
    search_fields = ("title",)
    filter_horizontal = ("categories",)
    inlines = [FileInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

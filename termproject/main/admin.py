from django.contrib import admin
from .models import Category, Item, ItemStoredHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ItemStoredHistoryInline(admin.TabularInline):
    model = ItemStoredHistory


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ItemStoredHistoryInline,
    ]

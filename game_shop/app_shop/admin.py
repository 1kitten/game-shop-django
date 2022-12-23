from django.contrib import admin
from .models import Shop, Item


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'shop']
    search_fields = ['title']

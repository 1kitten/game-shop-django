from django.contrib import admin
from .models import Profile, Royalty


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user.username']


@admin.register(Royalty)
class RoyaltyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

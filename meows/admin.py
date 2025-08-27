from django.contrib import admin
from .models import Meow

@admin.register(Meow)
class MeowAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_at')
    search_fields = ('body', 'author__username')
    list_filter = ('created_at',)

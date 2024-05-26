from django.contrib import admin

from products.models import Estate, File


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city')
    search_fields = ['title']
    list_filter = ['city']


class FileInlineAdmin(admin.TabularInline):
    model = File
    fields = ['id', 'title', 'file', 'order', 'is_active']
    extra = 0

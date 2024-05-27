from django.contrib import admin

from products.models import Estate, File


class FileInlineAdmin(admin.TabularInline):
    model = File
    fields = ['id', 'title', 'file', 'order', 'is_active']
    extra = 0


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city')
    search_fields = ['title']
    list_filter = ['city']
    inlines = [FileInlineAdmin]

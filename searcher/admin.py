from django.contrib import admin
from .models import Author


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('personal_name', 'alternate_names', 'view_count')
#
#
# admin.site.register(Author)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ['view_count', 'personal_name', 'alternate_names']
    ordering = ['-view_count']
    list_filter = ['view_count']
    search_fields = ['personal_name', 'alternate_names']

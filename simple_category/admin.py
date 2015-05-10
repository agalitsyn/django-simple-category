from django.contrib import admin

from models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['slug', 'name']
    list_filter = ['active']
    list_display = ['id', 'name',
                    'slug', 'parent',
                    'date_added', 'last_modified',
                    'active']

admin.site.register(Category, CategoryAdmin)

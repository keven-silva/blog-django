from django.contrib import admin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat')
    list_display_link = ('id', 'name_cat')


admin.site.register(Category, CategoryAdmin)

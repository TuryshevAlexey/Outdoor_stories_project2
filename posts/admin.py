from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'pub_date', 'author', 'category', 'photo'
    )
    list_filter = ('pub_date',)
    list_editable = ('category',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

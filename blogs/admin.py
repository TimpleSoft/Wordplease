# -*- coding: utf-8 -*-
from django.contrib import admin
from blogs.models import Post, Category

class PostAdmin(admin.ModelAdmin):

    list_filter = ('categories',)
    search_fields = ('title', 'abstract')
    list_display = ('title', 'abstract', 'imageUrl')

    fieldsets = (

        (None, {
            'fields': ('owner', 'title', 'publication_date'),
            'classes': ('wide',)
        }),

        ('Contenido', {
            'fields': ('abstract', 'body', 'imageUrl'),
            'classes': ('wide',)
        }),

        ('Extra', {
           'fields': ('categories',),
           'classes': ('wide', 'collapse')
        }),

    )

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
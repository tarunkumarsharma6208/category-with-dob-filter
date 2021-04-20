from django.contrib import admin
from .models import *


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ['name', 'dob']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['category', 'title']
    prepopulated_fields = {'slug': ('title',)}

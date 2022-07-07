from django.contrib import admin
from .models import *

class MusicAdmin(admin.ModelAdmin):
    list_display = ['title','duration','category','created_at']
    list_filter = ['category']
    search_fields = ['id']


# Register your models here.
admin.site.register(Category)
admin.site.register(Music,MusicAdmin)




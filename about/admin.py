from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content','created_on']
    list_filter = ('title','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

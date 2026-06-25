from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_on')
 
    summernote_fields = ('content',)

    def __str__(self):
        return self.title

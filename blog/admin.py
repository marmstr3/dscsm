from django.contrib import admin

from .models import Post, Tag
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextFields for Posts
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# Register Models
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

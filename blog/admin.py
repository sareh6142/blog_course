from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'datetime_created', 'datetime_modified')
    ordering = ('datetime_created',)

admin.site.register(Post,PostAdmin)
# Register your models here.

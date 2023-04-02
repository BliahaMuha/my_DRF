from django.contrib import admin
from .models import Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)


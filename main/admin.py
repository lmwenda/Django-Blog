from django.contrib import admin
from .models import Post, AdminsPost, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(AdminsPost)
admin.site.register(Comment)
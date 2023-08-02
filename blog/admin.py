from django.contrib import admin
from .models import Post
from .models import Article

admin.site.register(Article)
admin.site.register(Post)
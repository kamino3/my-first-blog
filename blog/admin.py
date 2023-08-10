from .models import Profile
from django.contrib import admin
from .models import Post
from .models import Article
from .models import ExamQuestion

admin.site.register(ExamQuestion)
admin.site.register(Article)
admin.site.register(Post)
admin.site.register(Profile)
from .models import Post, Article, ExamQuestion, Profile

from allauth.account.models import EmailConfirmation
admin.site.register(EmailConfirmation)
